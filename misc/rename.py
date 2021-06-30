import os
import sys
from os import listdir
from os.path import join, basename, split, splitext

s_path = input("Full Source Path: ")
if not len(s_path.split()) or s_path[0] != '/':
    print("Full Source path is required (eg. /home/cgalab/sessionx)")
    sys.exit(1)

session = input("Prefix name (eg. session1): ")
if not len(session.split()):
    print("Prefix name is required")
    sys.exit(1)

files = []

def path_leaf(path):
    head, tail = split(path)
    return tail or basename(head)

files += [fname for fname in listdir(s_path)]

for f in files:
    os.rename(join(s_path, f), join(s_path, session + '_' + f))