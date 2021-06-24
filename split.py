import random
train = 0.5
val = 0.2
test = 0.3
f = open("aaron.txt", "r")
trf = open("train.txt","a")
valf = open("val.txt","a")
testf = open("test.txt","a")
tvf = open("trainval.txt","a")
lines = f.readlines()
random.shuffle(lines)
for i in range(int(len(lines)*train)):
    trf.write(lines[i])
    tvf.write(lines[i])
for i in range(int(len(lines)*train), int(len(lines)*(train+val))):
    valf.write(lines[i])
    tvf.write(lines[i])
for i in range(int(len(lines)*(train+val)), len(lines)):
    testf.write(lines[i])
trf.close()
valf.close()
testf.close()
tvf.close()