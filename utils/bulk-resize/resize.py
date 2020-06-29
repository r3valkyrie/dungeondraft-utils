from sys import exit, argv
from os.path import join as joinpath
from os.path import basename
from glob import glob
from PIL import Image


def main(args):
    if not args:
        print('\nUsage: python resize.py [IMAGE, IMAGE, IMAGE] [DPI]\n'
              '\n'
              'IMAGE                    Can be any of: .jpg, .png.\n'
              'DPI                 The DPI or PPI of the asset(s).\n')
        return 0

    try:
        dpi = int(args.pop(-1))
    except ValueError:
        raise ValueError('DPI must be an integer.')

    if dpi < 256:
        while True:
            a = input('Upscaled images will appear blurry. Continue? (Y/n): ').lower()
            if a in ['y', 'yes']:
                break
            elif a in ['n', 'no']:
                return 0
            else:
                pass

    resize = (256 / dpi)

    if not args:
        for x in glob(joinpath('in', '*')):
            args.append((x, basename(x)))

    for path, name in args:
        print(f"Scaling image \"{name}\"", end="... ")
        with Image.open(path) as img:
            img = img.resize(
                (int((float(img.size[0]) * resize)),
                 int((float(img.size[1]) * resize))),
                Image.ANTIALIAS)
            img.save(joinpath('out', name))
        print('DONE')


if __name__ == '__main__':
    exit(main(argv[1:]))