import operator
import itertools
from time import time
from sys import maxint
import numpy as np

with open('data') as f:
    k,t = map(int,f.readline().strip().split())
    dataa = map(lambda x: x.strip(),f.readlines())

#Letter To Number
LTN = {'A':0,'C':1,'G':2,'T':3}
def MOST_FREQUENT_KMER(k,arr,data):
    def K_MER_PROP(Pattern):

        total=1
        for i in range(len(Pattern)):
            total*=arr[LTN[Pattern[i]]][i]
        return total
    #High probability
    HP = -1
    #Final Value (Gene)
    FV=''
    for i in range(len(data)-k+1):
        tmp = K_MER_PROP(data[i:i+k])
        if tmp>HP:
            HP = tmp
            FV = data[i:i+k]

    return FV

def GET_COUNT(motifs):
    count = np.zeros((4,len(motifs[0])))
    for i in range(len(motifs)):
        for j in range(len(motifs[0])):
            count[LTN[motifs[i][j]]][j]+=1
    return count+1

def GET_SCORE(motifs):
    count = GET_COUNT(motifs)
    total = np.sum(count)-np.sum(count[[np.argmax(count,axis=0)],[range(0,len(motifs[0]))]])
    return total

def GET_PROB(lst): 
    count = GET_COUNT(lst)
    pr =count/len(lst)
    return pr

bs = maxint
bm = []
for i in range(len(dataa[0])-k+1):
    motifs = []
    motifs.append(dataa[0][i:i+k])
    for j in range(1,t):
        cprob = GET_PROB(motifs)
        motifs.append(MOST_FREQUENT_KMER(k,cprob,dataa[j]))
    cs = GET_SCORE(motifs)
    if cs<bs:
        bs = cs
        bm = motifs

print '\n'.join(bm)

