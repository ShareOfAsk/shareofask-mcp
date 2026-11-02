#!/usr/bin/env python3
"""Validate local Markdown links, heading anchors and shipped PNG exports."""
from pathlib import Path
from urllib.parse import unquote, urlsplit
import re
import struct
import sys

ROOT = Path(__file__).resolve().parents[1]
LINK = re.compile(r'!?\[[^\]]*\]\(([^\s)]+)(?:\s+"[^"]*")?\)')
FENCE = re.compile(r'^\s*(```+|~~~+)')


def markdown_lines(path):
    fenced = False
    for number, line in enumerate(path.read_text(encoding='utf-8').splitlines(), 1):
        if FENCE.match(line):
            fenced = not fenced
            continue
        if not fenced:
            yield number, line


def anchors(path):
    found, counts = set(), {}
    for _, line in markdown_lines(path):
        heading = re.match(r'^#{1,6}\s+(.+?)\s*#*$', line)
        if heading:
            title = re.sub(r'\[([^\]]+)\]\([^)]+\)', r'\1', heading.group(1))
            slug = re.sub(r'[^\w\- ]', '', title.lower()).replace(' ', '-')
            count = counts.get(slug, 0)
            counts[slug] = count + 1
            found.add(slug if count == 0 else f'{slug}-{count}')
    return found


errors, checked = [], 0
files = sorted(p for p in ROOT.rglob('*.md') if '.git' not in p.parts and '.superpowers' not in p.parts)
for source in files:
    for number, line in markdown_lines(source):
        for match in LINK.finditer(line):
            target = urlsplit(match.group(1).strip('<>'))
            if target.scheme or target.netloc:
                continue
            destination = (source.parent / unquote(target.path)).resolve() if target.path else source
            checked += 1
            where = f'{source.relative_to(ROOT)}:{number}'
            if not destination.is_relative_to(ROOT):
                errors.append(f'{where}: link escapes repository: {match.group(1)}')
            elif not destination.exists():
                errors.append(f'{where}: missing file: {match.group(1)}')
            elif target.fragment and destination.suffix == '.md' and unquote(target.fragment) not in anchors(destination):
                errors.append(f'{where}: missing heading: {match.group(1)}')

images = ['hero', 'connect', 'agencies', 'marketing-teams', 'content-seo']
for name in images:
    path = ROOT / 'assets' / 'illustrations' / f'{name}.png'
    if not path.exists():
        errors.append(f'Missing illustration: {path.relative_to(ROOT)}')
        continue
    content = path.read_bytes()
    if content[:8] != b'\x89PNG\r\n\x1a\n' or len(content) < 24:
        errors.append(f'Invalid PNG: {path.relative_to(ROOT)}')
        continue
    width, height = struct.unpack('>II', content[16:24])
    if width < 1000 or height < 500:
        errors.append(f'Illustration is too small for readable documentation: {name} ({width}x{height})')

if errors:
    print('\n'.join(errors), file=sys.stderr)
    sys.exit(1)
print(f'PASS: {len(files)} Markdown files, {checked} local links/anchors, {len(images)} PNG exports.')
