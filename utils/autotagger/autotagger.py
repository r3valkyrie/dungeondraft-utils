from glob import glob
from json import dump
from os import makedirs
from os.path import abspath
from shutil import copy
from sys import exit


def main():
    in_path = abspath('./in')
    out_path = abspath('./out')
    for pack in glob(f'{in_path}/*'):
        dirs = [
            f'{out_path}/{pack.split("/")[-1]}/data',
            f'{out_path}/{pack.split("/")[-1]}/textures/objects'
        ]
        for x in dirs:
            makedirs(x, exist_ok=True)
        default = {'tags': {}, 'sets': {}}
        for tag in [x.split('/')[-1] for x in glob(f'{pack}/textures/objects/tags/*')]:
            default['tags'].update({tag: [
                f'textures/objects/{x.split("/")[-1]}' for x in glob(f'{pack}/textures/objects/tags/{tag}/*')
            ]})
        for img in glob(f'{pack}/textures/objects/**/*.png', recursive=True):
            copy(img, dirs[1])
        with open(f'{dirs[0]}/default.dungeondraft_tags', 'w+') as tagfile:
            dump(default, tagfile, sort_keys=False, indent=4)
    return 0


if __name__ == '__main__':
    exit(main())