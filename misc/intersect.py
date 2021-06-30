from os import listdir
from os.path import join, basename, split, splitext
import sys

PATH = input("Full Annotations Source Path: ")
if not len(PATH.split()) or PATH[0] != '/':
    print("Full Annotations Source path is required (eg. /home/cgalab/annotationsx)")
    sys.exit(1)

j_PATH = input("Full Images Source Path: ")
if not len(j_PATH.split()) or j_PATH[0] != '/':
    print("Full Images Source path is required (eg. /home/cgalab/sessionx)")
    sys.exit(1)

d_PATH = input("Full Images Destination Path: ")
if not len(d_PATH.split()) or d_PATH[0] != '/':
    print("Full Images Destination path is required (eg. /home/cgalab/sessionx)")
    sys.exit(1)

a_files = []

def path_leaf(path):
    head, tail = split(path)
    return tail or basename(head)

a_files += [fname for fname in listdir(PATH) if fname.endswith('.xml')]

for f in range(len(a_files)):
    a_files[f] = a_files[f].replace(".xml", "")


j_files = []
j_files += [fname for fname in listdir(j_PATH) if fname.endswith('.jpg')]

from shutil import copyfile


for f in j_files:
    f = f.replace(".jpg", "")
    if f in a_files:
        
        copyfile(join(j_PATH, f + ".jpg"), join(d_PATH,f + ".jpg"))