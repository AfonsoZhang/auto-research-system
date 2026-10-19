#!/usr/bin/env python3
"""Render authored D2/DOT/SVG to editable SVG, physical-size PDF and PNG."""
import argparse
import json
import math
import shutil
import subprocess
from pathlib import Path
from defusedxml import ElementTree as SafeET
from xml.etree import ElementTree as ET


def main():
    p = argparse.ArgumentParser(description=__doc__)
    p.add_argument('source', type=Path)
    p.add_argument('--out', type=Path, required=True, help='New output directory')
    p.add_argument('--width-mm', type=float, default=180)
    p.add_argument('--dpi', type=int, default=300)
    args = p.parse_args()
    if not math.isfinite(args.width_mm) or args.width_mm <= 0 or args.dpi < 72:
        p.error('Positive width and dpi >=72 required')
    import cairosvg
    import pymupdf as fitz
    source = args.source.resolve()
    if source.suffix.lower() not in ('.d2', '.dot', '.gv', '.svg') or not source.is_file():
        p.error('Source must be an existing D2, DOT/GV, or SVG file')
    args.out.mkdir(parents=False, exist_ok=False)
    svg = args.out / 'figure.svg'
    tools = Path(__file__).resolve().parents[4] / '.tools'
    if source.suffix.lower() == '.d2':
        d2 = tools / 'd2-v0.9.0/bin/d2'
        subprocess.run([str(d2), '--layout=dagre', '--pad=24', str(source), str(svg)], check=True)
        # D2 emits mask definitions beside rendered elements. CairoSVG paints
        # their children there; move definitions into defs without changing IDs.
        tree = SafeET.parse(svg)
        ns = '{http://www.w3.org/2000/svg}'
        ET.register_namespace('', ns[1:-1])
        for parent in list(tree.getroot().iter()):
            masks = [child for child in parent if child.tag == ns+'mask']
            if masks and parent.tag != ns+'defs':
                defs = ET.SubElement(parent, ns+'defs')
                for child in masks:
                    parent.remove(child)
                    defs.append(child)
        tree.write(svg, encoding='utf-8', xml_declaration=True)
    elif source.suffix.lower() in ('.dot', '.gv'):
        subprocess.run(['dot', '-Tsvg', str(source), '-o', str(svg)], check=True)
    else:
        shutil.copy2(source, svg)
    # CairoSVG default safe XML parsing; authored SVGs should embed local assets.
    pdf = args.out / 'figure.pdf'
    cairosvg.svg2pdf(url=str(svg), write_to=str(pdf), output_width=args.width_mm/25.4*96)
    with fitz.open(pdf) as doc:
        page = doc[0]
        page.get_pixmap(dpi=args.dpi).save(args.out / 'figure.png')
        report = {'source': str(source), 'width_mm':page.rect.width/72*25.4,
                  'height_mm':page.rect.height/72*25.4, 'dpi':args.dpi,
                  'pdf_has_extractable_text':bool(page.get_text().strip()),
                  'visual_review':'pending', 'collision_audit':'pending'}
    shutil.copy2(source, args.out / ('source'+source.suffix))
    (args.out/'render.json').write_text(json.dumps(report, indent=2)+'\n')
    print(json.dumps(report))


if __name__ == '__main__':
    main()
