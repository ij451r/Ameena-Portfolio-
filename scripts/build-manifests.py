#!/usr/bin/env python3
"""Rebuild manifest.json in every gallery folder. Run from the repo root: python scripts/build-manifests.py
Folders: work/school-posters and every folder inside work/brands. Hand-edited "alt" text is kept."""
import json, re
from pathlib import Path
try:
    from PIL import Image  # optional: adds width/height so the page does not jump while loading
except ImportError:
    Image = None
EXT = {'.jpg', '.jpeg', '.png', '.webp', '.avif', '.gif'}
ROOT = Path(__file__).resolve().parent.parent
FOLDERS = [ROOT/'work'/'school-posters', *sorted(p for p in (ROOT/'work'/'brands').iterdir() if p.is_dir())]
for d in FOLDERS:
    m, old = d/'manifest.json', {}
    if m.exists():
        try: old = {i['src']: i for i in json.loads(m.read_text('utf-8'))}
        except Exception: pass
    items = []
    for f in sorted(d.iterdir(), key=lambda p: p.name.lower()):
        if f.suffix.lower() not in EXT: continue
        src = f.relative_to(ROOT).as_posix()
        e = {'src': src, 'alt': old.get(src, {}).get('alt') or re.sub(r'[-_]+', ' ', f.stem).strip()}
        if Image:
            try:
                with Image.open(f) as im: e['w'], e['h'] = im.size
            except Exception: pass
        items.append(e)
    m.write_text(json.dumps(items, indent=2, ensure_ascii=False) + '\n', 'utf-8')
    print(f'{d.relative_to(ROOT)}: {len(items)} image(s)')
