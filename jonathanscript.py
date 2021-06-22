import fileinput
import os
from os import listdir
from os.path import join, basename, split, splitext
import sys

PATH="/Users/mac/Desktop/cgalab-transformation/annotations-old"
files = []

def path_leaf(path):
    head, tail = split(path)
    return tail or basename(head)

files += [join(PATH, fname) for fname in listdir(PATH) if join(PATH, fname).endswith('.xml')]

for file in files:
    xmin=0;ymin=0;xmax=0;ymax=0;
    new_file_name = file[:-(len(os.path.basename(file))+len("annotations-old/"))]+'annotations-new/new_'+os.path.basename(file)
    nf = open(new_file_name,"w")
    # memoize data
    
    for line in fileinput.input(file,inplace=0):
        if(line.startswith('<xmin>')):
            xmin=int(line[5:-7])
        elif(line.startswith('<ymin>')):
            ymin=int(line[5:-7])
        elif(line.startswith('<xmax>')):
            xmax=int(line[5:-7])
        elif(line.startswith('<ymax>')):
            ymax=int(line[5:-7])
        #insert alena's code

    #rewrite
    for line in fileinput.input(file,inplace=0):
        if(line.startswith('<xmin>')):
            nf.write('<xmin>'+xmin+'</xmin>')
        elif(line.startswith('<ymin>')):
            nf.write('<ymin>'+ymin+'</ymin>')
        elif(line.startswith('<xmax>')):
            nf.write('<xmax>'+ymin+'</xmax>')
        elif(line.startswith('<ymax>')):
            nf.write('<ymax>'+ymin+'</ymax>')
        else:
            nf.write(line)
    nf.close

        
        
        
