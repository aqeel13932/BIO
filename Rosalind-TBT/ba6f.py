import sys
import numpy as np
def ChromosomeToCycle(Chromosome):
    nodes=[]
    for j in range(len(Chromosome)):
        i = Chromosome[j]
        if i>0:
            nodes.append(2*i-1)
            nodes.append( 2*i)
        else:
            nodes.append(-2*i)
            nodes.append( -2*i-1)
    return nodes

if __name__ == "__main__":
    with open('data') as f:
        chrom = f.readline().strip()[1:-1].split()
        chrom = map(int,chrom)

    res = ChromosomeToCycle(chrom)
    res= map(str,res)
    with open('log.txt','w') as f:
        f.write('({})'.format(' '.join(res)))
