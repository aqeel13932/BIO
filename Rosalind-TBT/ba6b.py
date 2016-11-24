import sys
import numpy as np
def NumberOfBreakPoints(chrom):
    breakpoints=0
    chrom = [0]+chrom+[max(chrom)+1]
    for i in xrange(len(chrom)-1):
        if (chrom[i]+1)!=chrom[i+1]:
            breakpoints+=1
    return breakpoints
if __name__ == "__main__":
    with open('data') as f:
        chrom = f.readline().strip()[1:-1].split()
        chrom = map(int,chrom)
    res = NumberOfBreakPoints(chrom)
    with open('log.txt','w') as f:
        f.write('{}'.format(str(res)))
