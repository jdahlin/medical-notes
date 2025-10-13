#!/usr/bin/env python3
import os
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]

def compute_title_for_index(path: Path) -> str:
    parent = path.parent.name
    # Title-case first letter, keep diacritics
    if not parent:
        parent = 'Index'
    title = parent[:1].upper() + parent[1:]
    return f"{title} – översikt"

def ensure_frontmatter_title(text: str, title: str) -> str:
    if text.startswith('---'):
        # update existing title or add
        lines = text.splitlines()
        end = 1
        has_title = False
        while end < len(lines) and lines[end].strip() != '---':
            if lines[end].startswith('title:'):
                lines[end] = f"title: {title}"
                has_title = True
            end += 1
        if end < len(lines) and lines[end].strip() == '---':
            if not has_title:
                lines.insert(1, f"title: {title}")
            return '\n'.join(lines)
        # malformed frontmatter, prepend new
    # no frontmatter -> add
    return f"---\ntitle: {title}\n---\n\n" + text.lstrip('\n')

def ensure_h1(text: str, title: str) -> str:
    lines = text.splitlines()
    # Detect frontmatter
    if lines[:1] == ['---']:
        end = 1
        while end < len(lines) and lines[end].strip() != '---':
            end += 1
        if end < len(lines):
            # position after frontmatter block
            insert_at = end + 1
            # skip blank lines
            while insert_at < len(lines) and lines[insert_at].strip() == '':
                insert_at += 1
            if insert_at < len(lines) and lines[insert_at].startswith('# '):
                lines[insert_at] = f"# {title}"
            else:
                lines[insert_at:insert_at] = [f"# {title}", ""]
            return '\n'.join(lines) + ('\n' if text.endswith('\n') else '')
    # No frontmatter: ensure H1 at top
    i = 0
    while i < len(lines) and lines[i].strip() == '':
        i += 1
    if i < len(lines) and lines[i].startswith('# '):
        lines[i] = f"# {title}"
        return '\n'.join(lines) + ('\n' if text.endswith('\n') else '')
    return f"# {title}\n\n" + text

def fix_index_pages():
    for p in ROOT.rglob('_Index_.md'):
        text = p.read_text(encoding='utf-8')
        title = compute_title_for_index(p)
        # add/update frontmatter title
        t1 = ensure_frontmatter_title(text, title)
        # ensure first H1 present and correct
        t2 = ensure_h1(t1, title)
        # remove any duplicate frontmatter blocks beyond the first
        t3 = dedupe_extra_frontmatter(t2)
        if t3 != text:
            p.write_text(t3, encoding='utf-8')

def dedupe_extra_frontmatter(text: str) -> str:
    lines = text.splitlines()
    result = []
    i = 0
    # keep first frontmatter (if at top)
    if i < len(lines) and lines[i].strip() == '---':
        result.append(lines[i]); i += 1
        while i < len(lines):
            result.append(lines[i])
            if lines[i].strip() == '---':
                i += 1
                break
            i += 1
    # now copy the rest but strip any further '---' blocks
    in_block = False
    while i < len(lines):
        if lines[i].strip() == '---':
            in_block = not in_block
            i += 1
            continue
        if not in_block:
            result.append(lines[i])
        i += 1
    return '\n'.join(result) + ('\n' if text.endswith('\n') else '')

def remove_empty_dirs(root: Path):
    # remove empty directories bottom-up
    removed = True
    while removed:
        removed = False
        for d in sorted([p for p in root.rglob('*') if p.is_dir()], key=lambda x: len(str(x)), reverse=True):
            try:
                if not any(d.iterdir()):
                    d.rmdir()
                    removed = True
            except Exception:
                pass

def main():
    fix_index_pages()
    # cleanup likely old ascii dirs if empty
    for path in ['anatomi/karl', 'histologi/vavnad', 'histologi/kortlar']:
        d = ROOT / path
        if d.exists():
            remove_empty_dirs(d)
    # general sweep to remove empty leaf dirs
    remove_empty_dirs(ROOT)

if __name__ == '__main__':
    main()
