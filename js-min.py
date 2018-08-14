from __future__ import print_function
from __future__ import division

from glob import glob
import os
import sys
import argparse

is_win = 'win' in sys.platform

py_version = sys.version_info[0]

try:
    from slimit import minify
except:
    print("\nCannot import slimit. Try:")
    print("\npython -m pip install slimit\n")
    if is_win:
        print("If you need permission to install, open cmd as administrator")
    else:
        print("If you need permission, instead run")
        print("\nsudo python -m pip install slimit\n")
    
    print("If you run python with a command other than 'python', replace 'python' with the command you use above.\n")

    exit(1)

def read_files(directory):
    files = [f for f in glob(os.path.join(directory, "*")) if os.path.isfile(f)]
    dirs = [d for d in glob(os.path.join(directory, "*")) if os.path.isdir(d)]

    lines = []
    for f in files:
        lines += open(f, 'r').readlines()

    for d in dirs:
        lines += read_files(d)
    
    return lines

def save_file(filename, code):
    print("Saving {}".format(filename))
    out = open(filename, 'w')
    out.write(code)

def main():
    parser = argparse.ArgumentParser()
    parser.add_argument("--in-dir", dest="in_dir", type=str, default="_js/", help="The directory to recursively pull JS files from. Default = _js")
    parser.add_argument("--out-dir", dest="out_dir", type=str, default="assets/js/", help="The directory to output the minified and bundled JS to. Default = assets/js/")
    parser.add_argument("--filename", type=str, default="user.bundle.js", help="The name of the outputted js file. Default = user.bundle.js")
    parser.add_argument("--mangle", action="store_true", help="Include to rename variables and functions inside JS functions.")
    parser.add_argument("--mangle-toplevel", dest="mangle_toplevel", action="store_true", help="Include to rename variables and functions in global scope in JS files.")

    args = parser.parse_args()

    in_dir = args.in_dir
    out_dir = args.out_dir
    filename = args.filename
    mangle = args.mangle
    mangle_toplevel = args.mangle_toplevel

    lines = read_files(in_dir)
    
    code = " ".join(lines)
    code_size = sys.getsizeof(code)

    min_code = minify(code, mangle=mangle, mangle_toplevel=mangle_toplevel)
    min_size = sys.getsizeof(min_code)

    print("JS file size decreased by {:2.1f}%".format(100. * (code_size - min_size) / code_size))

    save_file(os.path.join(out_dir, filename), min_code)

if __name__ == "__main__":
    main()