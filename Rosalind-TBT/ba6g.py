import sys
import numpy as np
def CycleToChromosome(Nodes):
    output=[]
    i = 0 
    while i<len(Nodes):
        if Nodes[i]<Nodes[i+1]:
            output.append('+'+str(Nodes[i+1]/2))
        else:
            output.append('-'+str(Nodes[i]/2))
        i+=2
    '''                     
    for j in range(len(Nodes)/2):
        if Nodes[2*j-1]<Nodes[2*j]:
            output.append('+'+str(Nodes[2*j]/2))
        else:
            output.append('-'+str(Nodes[2*j-1]/2))
    '''
    return output

if __name__ == "__main__":
    with open('data') as f:
        chrom = f.readline().strip()[1:-1].split()
        chrom = map(int,chrom)
    res = CycleToChromosome(chrom)
    print res
    with open('log.txt','w') as f:
        f.write('({})'.format(' '.join(res)))
