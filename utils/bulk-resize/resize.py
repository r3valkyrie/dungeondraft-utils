import sys
import os
import glob

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
    in_path = os.path.abspath('./in')
    out_path = os.path.abspath('./out')

    if not args:
        args = glob.glob(f'{in_path}/*.png') + glob.glob(f'{in_path}/*.jpg')

    for path in args:
        name = path.split('/')[-1]
        print(f'Scaling image "{name}"', end='... ')
        try:
            with Image.open(path) as img:
                img = img.resize(
                    (int((float(img.size[0]) * resize)),
                     int((float(img.size[1]) * resize))),
                    Image.ANTIALIAS)
                img.save(f'{out_path}/{name}')
        except IOError:
            raise IOError

        print('DONE')


if __name__ == '__main__':
    sys.exit(main(sys.argv[1:]))