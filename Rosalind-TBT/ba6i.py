import sys
from ba6g import CycleToChromosome

def GraphToGenom(edges):
    
    sets =[]
    i=0
    while i<len(edges):
        tmp =[]
        while edges[i][0]<edges[i][1]:
            tmp.append(edges[i])
            i+=1
        tmp.append(edges[i])
        i+=1
        sets.append(tmp)
    for j in range(len(sets)):
        tmp =[]
        for i in range(len(sets[j])-1):
            tmp.append(sets[j][i][0])
            tmp.append(sets[j][i][1])
        tmp.append(sets[j][-1][0])
        tmp=[sets[j][-1][1]]+tmp
        sets[j] = CycleToChromosome(tmp)
    return sets

if __name__ == "__main__":
    with open('data') as f:
        edges = f.readline().strip().split('), (')
        edges[0]=edges[0][1:]
        edges[-1]= edges[-1][:-1]
        edges = [map(int,i.split(',')) for i in edges]



    res = GraphToGenom(edges)
    res = map(lambda x:'({})'.format( ' '.join(x)),res)
    res= map(str,res)
    with open('log.txt','w') as f:
        f.write('{}'.format(''.join(res)))
