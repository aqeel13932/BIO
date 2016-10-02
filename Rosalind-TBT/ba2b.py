import operator
import itertools
from time import time
from sys import maxint

with open('data') as f:
    k = int(f.readline().strip())
    data = map(lambda x :x.strip(),f.readlines())

words={}
#x = itertools.product(['A','C','G','T'],repeat=k)
#for i in x:
#        words[''.join(i)]=0



for i in range(len(data)):
    for j in range(len(data[i])-k+1):
        words[data[i][j:j+k]]=0
output={}

def HAMMINGDISTANCE(data1,data2):
    total = abs(len(data1)-len(data2))
    counter = min(len(data1),len(data2))
    for i in range (counter):
        total+= (data1[i]!=data2[i])
    return  total

def MINDISTANCE(Pattern,Dna):
    distance=maxint
    for i in range(len(Dna)-k+1):
        tmp =  HAMMINGDISTANCE(Pattern,Dna[i:i+k])
        if tmp<distance:
            distance =tmp
    return distance

for i in words.keys():
    words[i] = sum(map(lambda x: MINDISTANCE(i,x),data))


sorted_words = sorted(words.items(), key=operator.itemgetter(1),reverse=False)
basic =0
for i in range(len(sorted_words)):
    if i==0:
        print sorted_words[i][0],
        basic=sorted_words[i][0]
    elif sorted_words[i][1]==sorted_words[i-1][1]:
        print sorted_words[i][0],
    else:
        break
print ''
