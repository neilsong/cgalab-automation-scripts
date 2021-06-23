import fileinput
from os import listdir
from os.path import join, basename, split, splitext
import sys

PATH="/Users/alenazhang/Documents/cgalab-transformation/annotations-old"
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
    
    for line in fileinput.input(file):
        if '<xmin>' in line:
            line = line.replace(' ', '')
            line = line.replace('<xmin>', '')
            line = line.replace('</xmin', '')
            xmin = line
        elif line.startswith('<ymin>'):
            line = line.replace(' ', '')
            line = line.replace('<ymin>', '')
            line = line.replace('</ymin', '')
            ymin = line
        elif line.startswith('<xmax>'):
            line = line.replace(' ', '')
            line = line.replace('<xmax>', '')
            line = line.replace('</xmax', '')
            xmax = line
        elif line.startswith('<ymax>'):
            line = line.replace(' ', '')
            line = line.replace('<ymax>', '')
            line = line.replace('</ymax', '')
            ymax = line
        elif '<name>' in line:
            print('here')
            if 'R' in line:
                print('here2')
                handside=1
            elif 'L' in line:
                handside=0
            
            if '-' in line:
                if 'N' in line:
                    contactstate=0
                elif 'S' in line:
                    contactstate=1
                elif 'O' in line:
                    contactstate=2
                elif 'P' in line:
                    contactstate=3
                elif 'F' in line:
                    contactstate=0


    print(file)
    print(handside)

        
    for line in fileinput.input(file,inplace=1):
        if '<name>' in line and '>O<' not in line:
            print('        <name>hand</name>')
        elif '<difficult>' in line:
            print(line, end='')
            print('        <contactstate>'+str(contactstate)+"</constactstate>")
        else:
            print(line, end='')
        
