#!/usr/bin/env python3
import re
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]

def fmt_file(p: Path, rules):
    text = p.read_text(encoding='utf-8')
    orig = text
    for pat, repl in rules:
        text = re.sub(pat, repl, text, flags=re.MULTILINE)
    if text != orig:
        p.write_text(text, encoding='utf-8')

def main():
    f11 = ROOT / 'Målbeskrivning/1.1 Rörelseapparaten.md'
    f12 = ROOT / 'Målbeskrivning/1.2 Hjärta och cirkulation.md'

    if f11.exists():
      rules11 = [
        (r'^Lärandemål\s*$', '## Lärandemål\n'),
        (r'^Detaljerad målbeskrivning\s*$', '## Detaljerad målbeskrivning\n'),
        (r'^Anatomisk terminologi\s*$', '### Anatomisk terminologi\n'),
        (r'^Rörelseapparatens principer\s*$', '### Rörelseapparatens principer\n'),
        (r'^Rörelseapparatens ben, leder och muskler\s*$', '### Rörelseapparatens ben, leder och muskler\n'),
      ]
      fmt_file(f11, rules11)
      # Ensure file starts with a title
      text11 = f11.read_text(encoding='utf-8')
      if not text11.lstrip().startswith('# '):
          f11.write_text('# Rörelseapparatens anatomi (LPG001, block 1)\n\n' + text11, encoding='utf-8')

    if f12.exists():
      rules12 = [
        (r'^Lärandemål kursdel C.*Anatomi\s*$', '## Lärandemål (kursdel C/F) – Anatomi\n'),
        (r'^Hjärta\s*$', '## Hjärta\n'),
        (r'^Blodkärl\s*$', '## Blodkärl\n'),
      ]
      fmt_file(f12, rules12)
      # Bulletize linked lines under Hjärta and Blodkärl sections
      t12 = f12.read_text(encoding='utf-8')
      def bulletize_section(text, header):
          pattern = re.compile(rf'(^## {header}\s*$)(.*?)(^## |\Z)', re.M | re.S)
          def repl(m):
              head, body, tail = m.group(1), m.group(2), m.group(3)
              # add '- ' before lines starting with '[[' or alphabetic word followed by link
              body2 = re.sub(r'^(\[\[)', r'- \1', body, flags=re.M)
              body2 = re.sub(r'^(\*?\s*\w.*?\[\[)', r'- \1', body2, flags=re.M)
              return head + body2 + (tail or '')
          return pattern.sub(repl, text)
      t12 = bulletize_section(t12, 'Hjärta')
      t12 = bulletize_section(t12, 'Blodkärl')
      f12.write_text(t12, encoding='utf-8')

if __name__ == '__main__':
    main()
