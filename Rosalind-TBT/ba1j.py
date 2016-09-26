import operator
import itertools
from time import time
with open('data') as f:
    data = f.readline().strip()
    k,d = map(int,f.readline().strip().split())

match= {'A':'T','T':'A','G':'C','C':'G'}

def revdna(dna):
    ls = map(lambda x:match[x],list(dna))
    ls.reverse()
    return ''.join(ls)

words={}
x = itertools.product(['A','C','G','T'],repeat=k)
for i in x:
    words[''.join(i)]=0
def space(data1,data2):
    total = abs(len(data1)-len(data2))
    counter = min(len(data1),len(data2))
    for i in range (counter):
        total+= (data1[i]!=data2[i])
    return total

def registerAll(word):
    for i in range(len(data)-k+1):
        if space(data[i:i+k],word)<=d:
            words[word]+=1
        if space(data[i:i+k],revdna(word))<=d:
            words[word]+=1
i= 0
tt = len(words.keys())
for word in words.keys():
    registerAll(word)
    i+=1
    if (i%1000)==0:
        print i,tt

sorted_words = sorted(words.items(), key=operator.itemgetter(1),reverse=True)
outls=[]
for i in range(len(sorted_words)):
    if i==0:
        outls.append(sorted_words[i][0])
    elif sorted_words[i][1] == sorted_words[i-1][1]:
        outls.append(sorted_words[i][0])
    else:
        break

for val in outls:
    print val,


