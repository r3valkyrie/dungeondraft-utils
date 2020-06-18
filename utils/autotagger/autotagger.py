import sys
import os
import shutil
import glob
import json


def main():
    in_path = os.path.abspath('./in')
    out_path = os.path.abspath('./out')
    for pack in glob.glob(f'{in_path}/*'):
        dirs = [
            f'{out_path}/{pack.split("/")[-1]}/data',
            f'{out_path}/{pack.split("/")[-1]}/textures/objects'
        ]
        for x in dirs:
            os.makedirs(x, exist_ok=True)
        default = {'tags': {}, 'sets': {}}
        for tag in [x.split('/')[-1] for x in glob.glob(f'{pack}/textures/objects/tags/*')]:
            default['tags'].update({tag: [
                f'textures/objects/{x.split("/")[-1]}' for x in glob.glob(f'{pack}/textures/objects/tags/{tag}/*')
            ]})
        for img in glob.glob(f'{pack}/textures/objects/**/*.png', recursive=True):
            shutil.copy(img, dirs[1])
        with open(f'{dirs[0]}/default.dungeondraft_tags', 'w+') as tagfile:
            json.dump(default, tagfile, sort_keys=False, indent=4)
    return 0


if __name__ == '__main__':
    sys.exit(main())