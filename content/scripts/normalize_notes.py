#!/usr/bin/env python3
import os
import re
import shutil
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]

# Target only markdown content
def iter_md_files(root: Path):
    for p in root.rglob('*.md'):
        # Skip hidden dirs (e.g., .git) and virtualenvs
        if any(part.startswith('.') for part in p.parts):
            continue
        yield p

# Map ASCII segments -> Swedish diacritics (only for known names we used)
REPLACEMENTS = {
    'vavnad': 'vävnad',
    'bindvav': 'bindväv',
    'kortlar': 'körtlar',
    'karl': 'kärl',
    'overarm': 'överarm',
    'overgangsepitel-urotel': 'övergångsepitel-urotel',
    'respirationsvagsepitel': 'respirationsvägsepitel',
    'tradbrosk': 'trådbrosk',
    'retikular': 'retikulär',
    'forhornat': 'förhornat',
    'oforhornat': 'oförhornat',
    'tat-oregelbunden': 'tät-oregelbunden',
    'tat-regelbunden': 'tät-regelbunden',
    'mukos': 'mukös',
    'seros': 'serös',
    'seromukos': 'seromukös',
    'endokrin-follikular-typ': 'endokrin-follikulär-typ',
    'endokrin-strangtyp': 'endokrin-strängtyp',
    'bagarcell': 'bägarcell',
    'vit-fettvav': 'vit-fettväv',
    'brun-fettvav': 'brun-fettväv',
}

def apply_diacritics(seg: str) -> str:
    s = seg
    for k, v in REPLACEMENTS.items():
        if k in s:
            s = s.replace(k, v)
    # Second-pass quick fixes for prior Title-Cased names
    s = s.replace('Tat ', 'Tät ')
    s = s.replace('Forhornat', 'Förhornat')
    return s

def to_title_with_spaces(filename_base: str) -> str:
    # Preserve special index pages verbatim
    if filename_base == '_Index_':
        return filename_base
    # Replace hyphens with spaces
    s = filename_base.replace('-', ' ')
    # Collapse whitespace
    s = re.sub(r'\s+', ' ', s).strip()
    # Title Case each word
    s = ' '.join(w.capitalize() for w in s.split(' '))
    return s

def compute_new_path(old_path: Path) -> Path:
    rel = old_path.relative_to(ROOT)
    parts = list(rel.parts)
    new_parts = []
    for i, seg in enumerate(parts):
        # File segment with extension
        if i == len(parts) - 1 and seg.endswith('.md'):
            base = seg[:-3]
            base = apply_diacritics(base)
            base = to_title_with_spaces(base)
            new_parts.append(base + '.md')
        else:
            seg2 = apply_diacritics(seg)
            # Keep folder names as-is except diacritics; avoid title-case for common folders
            new_parts.append(seg2)
    return ROOT.joinpath(*new_parts)

def build_rename_map():
    mapping = {}
    for p in iter_md_files(ROOT):
        newp = compute_new_path(p)
        if newp != p:
            mapping[p] = newp
    return mapping

WIKILINK_RE = re.compile(r"\[\[([^\]|]+)(\|[^\]]+)?\]\]")

def strip_leading_h1(text: str) -> str:
    lines = text.splitlines()
    i = 0
    # Skip leading blank lines
    while i < len(lines) and lines[i].strip() == '':
        i += 1
    if i < len(lines) and lines[i].lstrip().startswith('# '):
        # Drop this H1 line
        i += 1
        # If the next is blank, drop a single blank too
        if i < len(lines) and lines[i].strip() == '':
            i += 1
        return '\n'.join(lines[i:]) + ('\n' if text.endswith('\n') else '')
    return text

def rel_without_ext(p: Path) -> str:
    return str(p.relative_to(ROOT).with_suffix('')).replace('\\', '/')

def update_wikilinks(content: str, path_map_rel: dict) -> str:
    def repl(m):
        target = m.group(1).strip()
        alias = m.group(2) or ''  # includes leading '|'
        # Normalize target (strip potential .md)
        t = target[:-3] if target.endswith('.md') else target
        new = path_map_rel.get(t)
        if new:
            return f"[[{new}{alias}]]"
        return m.group(0)
    return WIKILINK_RE.sub(repl, content)

def main():
    # 1) Build rename map
    rename_map = build_rename_map()

    # Map for link updates: old_rel_noext -> new_rel_noext
    link_map = {}
    for old, new in rename_map.items():
        link_map[rel_without_ext(old)] = rel_without_ext(new)

    # 2) Rename paths (deepest first)
    for old, new in sorted(rename_map.items(), key=lambda kv: len(str(kv[0]).split(os.sep)), reverse=True):
        new.parent.mkdir(parents=True, exist_ok=True)
        shutil.move(str(old), str(new))

    # 3) Rewrite content in all md files: strip leading H1 and update wikilinks
    for p in iter_md_files(ROOT):
        text = p.read_text(encoding='utf-8')
        new_text = strip_leading_h1(text)
        new_text = update_wikilinks(new_text, link_map)
        if new_text != text:
            p.write_text(new_text, encoding='utf-8')

if __name__ == '__main__':
    main()
