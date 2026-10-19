#!/usr/bin/env python3
"""Check effective PDF span sizes after Cairo/SVG text transforms, not raw Tf."""
import argparse
import json
import pymupdf


def audit(pdf, minimum=5.0):
    runs = []
    image_blocks = 0
    with pymupdf.open(pdf) as doc:
        for i, page in enumerate(doc):
            for block in page.get_text('dict')['blocks']:
                if block.get('type') == 1:
                    image_blocks += 1
                for line in block.get('lines', []):
                    for span in line['spans']:
                        if span['text'].strip():
                            runs.append({'page':i+1, 'text':span['text'],
                                         'size_pt':span['size'], 'bbox':span['bbox']})
    below = [x for x in runs if x['size_pt'] < minimum-0.01]
    return {'verdict':'NOT AUDITABLE' if not runs else 'FAIL' if below else 'PASS',
            'scope':'extractable PDF text only; inspect raster/outlined labels visually',
            'min_required_pt':minimum, 'min_found_pt':min((x['size_pt'] for x in runs),default=None),
            'text_runs':len(runs), 'image_blocks':image_blocks, 'below_minimum':below}


if __name__ == '__main__':
    p=argparse.ArgumentParser(description=__doc__)
    p.add_argument('pdf')
    p.add_argument('--min-pt',type=float,default=5.0)
    args=p.parse_args()
    r=audit(args.pdf,args.min_pt)
    print(json.dumps(r,ensure_ascii=False,indent=2))
    raise SystemExit({'PASS':0,'FAIL':1,'NOT AUDITABLE':2}[r['verdict']])
