import operator
import itertools
from time import time
def space(data1,data2):
    total = abs(len(data1)-len(data2))
    counter = min(len(data1),len(data2))
    for i in range (counter):
        total+= (data1[i]!=data2[i])
    return total

with open('data') as f:
    data = f.readline().strip()
    d = int(f.readline().strip())
words={}
x = itertools.product(['A','T','G','C'],repeat=len(data))

for i in x:
    perm = ''.join(i)
    if space(data,perm)<=d:
        print perm


