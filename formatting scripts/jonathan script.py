import fileinput
from os import listdir
from os.path import join, basename, split, splitext
import sys
import math

o_PATH="/Users/mac/Desktop/cgalab-transformation/annotations-old"
PATH="/home/cgalab/annotations-copy"
files = []

def path_leaf(path):
    head, tail = split(path)
    return tail or basename(head)

files += [join(PATH, fname) for fname in listdir(PATH) if join(PATH, fname).endswith('.xml')]

class Object(object):
    xmin=0
    ymin=0
    xmax=0
    ymax=0
    isObject = True#set default

    def xcenter(self):
        return (self.xmin+self.xmax+1)/2
    def ycenter(self):
        return (self.ymin+self.ymax+1)/2
    
class hand(Object):
    portable = -1
    handside = -1
    contactstate = -1
    def dx(self):
        return self.portable.xcenter()-self.xcenter()
    def dy(self):
        return self.portable.ycenter()-self.ycenter()
    def mag(self):
        return math.sqrt(self.dx()*self.dx()+self.dy()*self.dy())

for file in files:
    # memoize data
    objArr = []
    temp = Object()
    for line in fileinput.input(file,inplace=0):
        
        if "</object>" in line:
            objArr.append(temp)
            temp = Object()
        elif '<xmin>' in line:
            line = line.replace(' ', '')
            line = line.replace('<xmin>', '')
            line = line.replace('</xmin>', '')
            line = line.replace('\t','')
            line = line.replace('\n','')
            temp.xmin = int(line)
        elif '<ymin>' in line:
            line = line.replace(' ', '')
            line = line.replace('<ymin>', '')
            line = line.replace('</ymin>', '')
            line = line.replace('\t','')
            line = line.replace('\n','')
            temp.ymin = int(line)
        elif '<xmax>' in line:
            line = line.replace(' ', '')
            line = line.replace('<xmax>', '')
            line = line.replace('</xmax>', '')
            line = line.replace('\t','')
            line = line.replace('\n','')
            temp.xmax = int(line)
        elif '<ymax>' in line:
            line = line.replace(' ', '')
            line = line.replace('<ymax>', '')
            line = line.replace('</ymax>', '')
            line = line.replace('\t','')
            line = line.replace('\n','')
            temp.ymax = int(line)
        elif '<name>' in line:
            print('here')
            if '-' in line:
                temp = hand()
                temp.isObject=False
                if 'R' in line:
                    temp.handside=1
                elif 'L' in line:
                    temp.handside=0
                
                if 'N' in line:
                    temp.contactstate=0
                elif 'S' in line:
                    temp.contactstate=1
                elif 'O' in line:
                    temp.contactstate=2
                elif 'P' in line:
                    temp.contactstate=3
                elif 'F' in line:
                    temp.contactstate=0
                print("ct state " + str(temp.contactstate))
            elif 'O' in line:
                temp = Object()
                temp.isObject=True

    print(file)
    i = 0
    temp = Object()
    test = hand()
    test.portable = Object()
    test.isObject = False
    objArr.append(test)
    for line in fileinput.input(file,inplace=1):
        if '<name>' in line:
            temp = objArr[i]
            if '>O<' not in line:
                print('        <name>hand</name>')
                temp = objArr[i]
                if not temp.isObject and 'P' in line:
                    for e in objArr:
                        if e.isObject:
                            dx = e.xcenter()-temp.xcenter()
                            dy = e.ycenter()-temp.ycenter()
                            mag = math.sqrt(dx*dx+dy*dy)
                            if temp.portable==-1 or mag < temp.mag():
                                temp.portable = e
            else:
                print('        <name>targetobject</name>')
            i+=1
        elif '<difficult>' in line:
            print(line, end='')
            if not temp.isObject:
                print('        <contactstate>'+str(temp.contactstate)+"</contactstate>")
            else:
                print('        <contactstate></contactstate>')
            if not temp.isObject and temp.portable != -1:
                unitdx = float(temp.dx())/temp.mag()
                unitdy = float(temp.dy())/temp.mag()
                print("        <unitdx>"+str(unitdx)+"</unitdx>")
                print("        <unitdy>"+str(unitdy)+"</unitdy>")
                print("        <magnitude>"+str(temp.mag())+"</magnitude>")
            else:
                print("        <unitdx></unitdx>")
                print("        <unitdy></unitdy>")
                print("        <magnitude></magnitude>")
            contact = [ obj.handside for obj in objArr if not obj.isObject and obj.portable == temp]
            if temp.isObject and len(contact):
                if 0 in contact:
                    print("        <contactleft>1</contactleft>")
                else:
                    print("        <contactleft></contactleft>")
                if 1 in contact:
                    print("        <contactright>1</contactright>")
                else:
                    print("        <contactright></contactright>")
                

            
            if not temp.isObject:
                print("        <handside>"+str(temp.handside)+"</handside>")
            else:
                print("        <handside></handside>")
        elif '</bndbox>' in line:
            print(line, end='')
            if not temp.isObject and temp.portable != -1:
                print("        <objxmin>" + str(temp.portable.xmin) + "</objxmin>")
                print("        <objymin>" + str(temp.portable.ymin) + "</objymin>")
                print("        <objxmax>" + str(temp.portable.xmax) + "</objxmax>")
                print("        <objymax>" + str(temp.portable.ymax) + "</objymax>")
            else:
                print("        <objxmin></objxmin>")
                print("        <objymin></objymin>")
                print("        <objxmax></objxmax>")
                print("        <objymax></objymax>")
                
        else:
            print(line, end='')
            