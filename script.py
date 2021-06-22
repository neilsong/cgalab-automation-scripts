import fileinput
from os import listdir
from os.path import join, basename, split, splitext
import sys

PATH="/Users/mac/Desktop/cgalab-transformation"
files = []

def path_leaf(path):
    head, tail = split(path)
    return tail or basename(head)

files += [join(PATH, fname) for fname in listdir(PATH) if join(PATH, fname).endswith('.xml')]


for file in files:
    global xmin

    # memoize data
    for line in fileinput.input(file,inplace=0):
        if line.startswith('<xmin>'):
            xmin=int(line[5:-7])
        elif line.startswith('<ymin>'):
            ymin=int(line[5:-7])
        elif line.startswith('<xmax>'):
            xmax=int(line[5:-7])
        elif line.startswith('<ymax>'):
            ymax=int(line[5:-7])
