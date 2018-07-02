#
# Usage: this script converts all of the images located in _img/<folder>
#        to responsive sizes places them into assets/img/<folder>. The 
#        default behavior will make no attempt to convert JPG images to PNG 
#        or PNG images to JPG, however this behavior is implemented and can be 
#        referenced by running this script with the --help or -h options.
#

from __future__ import print_function
from __future__ import division
from builtins import input

import sys
import os
import shutil
from glob import glob
from PIL import Image
import argparse

class bcolors:
    HEADER = '\033[95m'
    OKBLUE = '\033[94m'
    OKGREEN = '\033[92m'
    WARNING = '\033[93m'
    FAIL = '\033[91m'
    ENDC = '\033[0m'
    BOLD = '\033[1m'
    UNDERLINE = '\033[4m'

resize_widths = {
    "placehold" : 230,
    "thumb" : 535,
    "thumb@2x" : 535 * 2,
    "xs" : 575,
    "sm" : 767,
    "md" : 991,
    "lg" : 1999,
    "self" : -1
}

def make_dir(save_dir):
    if not os.path.exists(save_dir):
        os.makedirs(save_dir)

def update(msg):
    print(bcolors.OKBLUE + msg + bcolors.ENDC)

def warn(msg):
    msg_lines = msg.split("\n")
    print('    ' + bcolors.WARNING + "WARNING: " + msg_lines[0] + bcolors.ENDC)
    for msg_line in msg_lines[1:]:
        print('    ' + bcolors.WARNING + "         " + msg_line + bcolors.ENDC)

def error(msg):
    msg_lines = msg.split("\n")
    print('\n' + bcolors.FAIL + "ERROR: " + msg_lines[0] + bcolors.ENDC)
    for msg_line in msg_lines[1:]:
        print(bcolors.FAIL + "       " + msg_line + bcolors.ENDC)    
    print()

def save(img, fn, format, quality):
    print('    ' + bcolors.OKGREEN + "Saving: " + fn + bcolors.ENDC)
    img.save(fn, format, optimize=True, quality=quality)

def main():
    parser = argparse.ArgumentParser()
    parser.add_argument("--convert", type=str, action='store',
        help="The format to convert all images to. Either JPEG or PNG.",
        default=None)
    parser.add_argument("--quality", type=int, action='store',
        help="The quality to use with JPEG compression. Valid range is 1 - 100.",
        default=70)
    parser.add_argument("--out-dir", type=str, action='store', dest='out_dir',
        help="The root directory to send resized pictures to.",
        default=os.path.join("assets", "img"))
    parser.add_argument("--in-dir", type=str, action='store', dest='in_dir', 
        help="The root directory to pull pictures from.",
        default="_img")
    parser.add_argument("--clean", action='store_true', default=False,
        help="Include this to clean the output directory (assets/img) by default.")
    parser.add_argument("--shallow", action='store_true', default=False,
        help="Include this to only write images that don't already exist.")

    args = parser.parse_args()

    in_dir = args.in_dir
    out_dir = args.out_dir

    convert = args.convert
    quality = args.quality
    clean = args.clean
    shallow = args.shallow

    if clean:
        if out_dir in ['.', './']:
            warn("You are attempting to remove the current directory!!")
        else:
            warn("You are attempting to remove the directory {}".format(out_dir))
        
        ans = input("Are you sure you want to do this? [yes / no]: ")
        if ans.lower() in ['yes', 'y']:
            # Delete only folders that exist in in_dir
            in_dir_folder_names = [os.path.basename(f) for f in glob(os.path.join(in_dir, '*')) if os.path.isdir(f)]
            out_dir_folders = [os.path.join(out_dir, f) for f in in_dir_folder_names]
            for f in out_dir_folders:
                warn("Removing folder: {}".format(f))
                shutil.rmtree(f)

    # Check for spelling error
    if convert is None:
        pass
    elif convert.lower() in ['jpg', 'jpeg']:
        convert = 'JPEG'
    elif convert.lower() in ['png']:
        convert = 'PNG'
    elif convert is not None:
        error("value passed to --convert not valid. Use {} --help for more info.".format(sys.argv[0]))
        exit()

    # Range checking
    if quality > 100 or quality < 1:
        error("value passed to --quality not valid. Use {} --help for more info.".format(sys.argv[0]))
        exit()
    
    # Loop through all folders including the root folder
    folders = [f for f in glob(os.path.join(in_dir, "*")) if os.path.isdir(f)] + [in_dir]
    for folder in folders:
        folder_name = os.path.basename(folder)
        # Check if we are scanning the root directory, in which case we want
        # those files to go to the root of the our directory
        if folder_name == in_dir:
            save_dir = out_dir
        else:
            save_dir = os.path.join(out_dir, folder_name)
        
        make_dir(save_dir)

        jpgs = glob(os.path.join(folder, "*.jpg"))
        pngs = glob(os.path.join(folder, "*.png"))

        image_names = jpgs + pngs
        images = [Image.open(i) for i in jpgs] + [Image.open(i) for i in pngs]

        for name, img in zip(image_names, images):
            update("\nProcessing {}".format(name))
            if img.format not in ['JPEG', 'PNG']:
                warn("image is required to be either JPEG or PNG format.\nSkipping...")

            width = img.width
            height = img.height

            aspect_ratio = float(width) / float(height)

            for width_name, resize_width in sorted(resize_widths.iteritems(), key=lambda (k, v) : (v, k)):
                filename, ext = os.path.splitext(name)

                if img.format == 'JPEG' or convert == 'JPEG':
                    ext = 'jpg'
                elif img.format == 'PNG' or convert == 'PNG':
                    ext = 'png'

                if width_name == 'self':
                    save_name = "{}.{}".format(os.path.join(save_dir, os.path.basename(filename)), ext)                
                else:
                    save_name = "{}_{}.{}".format(os.path.join(save_dir, os.path.basename(filename)), 
                        width_name, ext)

                # If we don't want to overwrite images, skip ones that already exist
                if shallow and os.path.exists(save_name):
                    update("Skipping existing file!")
                    continue

                # Compute necessary height given aspect ratio
                resize_height = int(resize_width / aspect_ratio)

                # Check if we are upscaling, in which case a new image isn't necessary
                if resize_width >= width:
                    warn("upscaling detected! Format {} requires an image of width at least {}px\nsaving at normal resolution...".format(width_name, resize_width))
                    resize_width = width
                    resize_height = height

                if width_name == 'self':
                    resize_width = width
                    resize_height = height

                resized_img = img.resize((resize_width, resize_height))

                # Check if we need to convert the image before saving
                if convert is not None:
                    if convert == 'JPEG':
                        resized_img = resized_img.convert('RGB')
                    elif convert == 'PNG':
                        resized_img = resized_img.convert('RGBA')

                    save(resized_img, save_name, convert, quality)
                else:
                    save(resized_img, save_name, img.format, quality)
    
if __name__ == "__main__":
    main()