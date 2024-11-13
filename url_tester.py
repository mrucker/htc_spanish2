from pathlib import Path
import json

def recurse(obj):
    if isinstance(obj,dict):
        for k,v in obj.items():
            if 'url' in k.lower() and not Path(f'.{v}').exists():
                yield v
            else:
                yield from recurse(v)
    if isinstance(obj,list):
        for o in obj:
            yield from recurse(o)

for p in Path('./scripts').iterdir():
    with open(p, encoding='utf-8') as f:
        
        bad_links = list(recurse(json.load(f)))

        if bad_links:
            print(p.stem)
            for l in bad_links:
                print(f'  {l}')
