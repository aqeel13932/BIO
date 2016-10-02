import operator
import itertools
from time import time

with open('data') as f:
    k,d = map(int,f.readline().strip().split())
    data = map(lambda x :x.strip(),f.readlines())

words={}
x = itertools.product(['A','C','G','T'],repeat=k)
for i in x:
        words[''.join(i)]=0

output={}

def HAMMINGDISTANCE(data1,data2):
    total = abs(len(data1)-len(data2))
    counter = min(len(data1),len(data2))
    for i in range (counter):
        total+= (data1[i]!=data2[i])
    return  total

def IsInDistance(val,dat,maxd):
    for i in range(len(dat)-k+1):
        if HAMMINGDISTANCE(val,dat[i:i+k])<=maxd:
            val,dat[i:i+k+1]
            return True
    return False

def ADDTOLIST(diction , Pattern):
    if Pattern in diction.keys():
        diction[Pattern]+=1
    else:
        diction[Pattern]=1



for val in words.keys():
    totaok=0
    for dat in data:
        if IsInDistance(val,dat,d):
            totaok+=1
        else:
            break
    if totaok==len(data):
        ADDTOLIST(output,val)
print ' '.join(output.keys())
