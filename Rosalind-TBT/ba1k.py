import itertools
from collections import OrderedDict
with open('data') as f:
    data = f.readline().strip()
    k = int(f.readline().strip())

x = itertools.product(['A','C','G','T'],repeat=k)
val = OrderedDict()
for i in x:
    val[''.join(i)]=0

for i in range(len(data)-k+1):
    val[data[i:i+k]]+=1

for i in val.keys():
    print val[i],
print ''
