import fileinput
from os import listdir
from os.path import join, basename, split, splitext
import sys

PATH="/Users/Bill/Desktop/cgalab-transformation"
files = []

def path_leaf(path):
    head, tail = split(path)
    return tail or basename(head)

files += [join(PATH, fname) for fname in listdir(PATH) if join(PATH, fname).endswith('.xml')]


for file in files:
    global xmin
    global handside
    global contactstate
    # memoize data
    #rewrite
    
    for line in fileinput.input(file,inplace=0):
        if line.startswith('<xmin>'):
            xmin=int(line[5:-7])
        elif line.startswith('<ymin>'):
            ymin=int(line[5:-7])
        elif line.startswith('<xmax>'):
            xmax=int(line[5:-7])
        elif line.startswith('<ymax>'):
            ymax=int(line[5:-7])
        elif line.startswith('<name>'):
            if (line[6]=='R'):
                handside=1
            elif (line[6]=='L'):
                handside=0
            
            if (line[7]=='-'):
                if (line[8]=='N'):
                    contactstate=0
                elif (line[8]=='S'):
                    contactstate=1
                elif (line[8]=='O'):
                    contactstate=2
                elif (line[8]=='P'):
                    contactstate=3


        
        
    for line in fileinput.input(file,inplace=1):
        if line.startswith('<name>'):
            print("<name>"+handside+"</name>")
        elif line.startswith('<contactstate>'):
            print("<contactstate>"+contactstate+"</constactstate>")
        
