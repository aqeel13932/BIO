import sys
from ba6f import ChromosomeToCycle

def ColoredEdges(P):
    Edges = []
    for chrom in P:

        Nodes = ChromosomeToCycle(chrom)
        Nodes.append(Nodes[0])
        Nodes = Nodes[1:]
        for j in range(len(chrom)):
            Edges.append((Nodes[2*j],Nodes[2*j+1]))
    return Edges

if __name__ == "__main__":
    with open('data') as f:
        chromss = f.readline().strip().split(')(')
        chromss[0]= chromss[0][1:]
        chromss[-1]=chromss[-1][:-1]
        for i in range(len(chromss)):
            chromss[i]= chromss[i].split()
            chromss[i]= map(int,chromss[i])

    res = ColoredEdges(chromss)
    res= map(str,res)
    with open('log.txt','w') as f:
        f.write('{}'.format(', '.join(res)))
