from os import listdir
from os.path import join, basename, split, splitext

PATH="/home/cgalab/annotations"
a_files = []

def path_leaf(path):
    head, tail = split(path)
    return tail or basename(head)

a_files += [fname for fname in listdir(PATH) if fname.endswith('.xml')]

for f in range(len(a_files)):
    a_files[f] = a_files[f].replace(".xml", "")


j_PATH="/home/cgalab/session4"
j_files = []
j_files += [fname for fname in listdir(j_PATH) if fname.endswith('.jpg')]
d_PATH="/home/cgalab/session"

from shutil import copyfile


for f in j_files:
    f = f.replace(".jpg", "")
    if f in a_files:
        
        copyfile(j_PATH + '/' + f + ".jpg", d_PATH + '/'+ f + ".jpg")