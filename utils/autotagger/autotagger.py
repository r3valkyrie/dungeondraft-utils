from json import dump as dumpjson
from os import makedirs, listdir
from os.path import join as joinpath
from shutil import copy as copyfiles
from sys import exit


def main():
    for pack in listdir('in'):
        if pack[0] != '.':
            for outdir in [joinpath('out', pack, 'data'),
                           joinpath('out', pack, 'textures', 'objects')]:
                makedirs(outdir, exist_ok=True)

            default = {'tags': {}, 'sets': {}}
            for tag in listdir(joinpath('in', pack, 'textures', 'objects', 'tags')):
                default['tags'].update({tag: [
                    f"textures/objects/{x}" for x in listdir(joinpath('in', pack, 'textures', 'objects', 'tags', tag))
                ]})
                for x in listdir(joinpath('in', pack, 'textures', 'objects', 'tags', tag)):
                    copyfiles(joinpath('in', pack, 'textures', 'objects', 'tags', tag, x),
                              joinpath('out', pack, 'textures', 'objects'))
            with open(joinpath('out', pack, 'data', 'default.dungeondraft_tags'), 'w+') as tagfile:
                dumpjson(default, tagfile, sort_keys=False, indent=4)
    return 0


if __name__ == '__main__':
    exit(main())