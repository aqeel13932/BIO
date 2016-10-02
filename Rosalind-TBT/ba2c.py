import operator
import itertools
from time import time
from sys import maxint
import numpy as np
with open('data') as f:
    dataa = f.readline().strip()
    kk = int(f.readline().strip())
    arrr = np.zeros((4,kk))
    for i in range(4):
        arrr[i] = map(float,f.readline().strip().split())
def MOST_FREQUENT_KMER(k,arr,data):
    #Letter To Number
    LTN = {'A':0,'C':1,'G':2,'T':3}


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

    print FV
MOST_FREQUENT_KMER(kk,arrr,dataa)
