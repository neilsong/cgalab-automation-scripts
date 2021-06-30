from os.path import join, basename, split, splitext
import sys
import math
import os
from os import listdir

PATH=os.getcwd()
files = []

def path_leaf(path):
    head, tail = split(path)
    return tail or basename(head)

files += [join(PATH, fname) for fname in listdir(PATH) if join(PATH, fname).endswith('.pkl')]

import pickle
import numpy
raw = {}
for i in files:
    raw[i] = pickle.load(open(i, "rb"))

# output to file
with open("info.txt", 'w') as f:
    for key, value in raw.items(): 
        f.write('%s:%s\n' % (key, value))