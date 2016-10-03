import operator
import itertools
from time import time
from sys import maxint
import numpy as np
from random import randint
with open('data') as f:
    km,tm = map(int,f.readline().strip().split())
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

def GET_MFK_ALL(k,arr,data):
    return map(lambda x: MOST_FREQUENT_KMER(k,arr,x),data)

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

def RANDOMIZEDMOTIFSEARCH(Dna,k,t):
    bs = maxint
    bm = []
    #Randomly Select the start point
    rand_ints = [randint(0,len(Dna[0])-k) for a in xrange(t)]
    motifs = [dataa[i][r:r+k] for i,r in enumerate(rand_ints)]
    #motifs = map(lambda x: Dna[0][x:x+k],Rs)
    bs = GET_SCORE(motifs)
    bm = motifs
    while True:
        cprob = GET_PROB(motifs)
        motifs= GET_MFK_ALL(k,cprob,Dna)
        cs = GET_SCORE(motifs)
        if cs<bs:
            bs = cs
            bm = motifs
        else:
            return bs,bm

#global best score
gbs = maxint
gbm = []
for i in range(0,1000):
    if i%100 ==0:
        print i
    tbs,tbm = RANDOMIZEDMOTIFSEARCH(dataa,km,tm)
    if tbs<gbs:
        gbs=tbs
        gbm = tbm
print '\n'.join(gbm)
with open('log.out','w') as output:
    output.write('\n'.join(gbm))
