from collections import defaultdict
def FindPath(Graphv):
    def InOutCounter(Graphv):
        counter={}
        for v in Graphv:
            if v in counter:
                counter[v]=(counter[v][0],counter[v][1]+1)
            else:
                counter[v]=(0,1)
            for dest in Graphv[v]:
                if dest in counter:
                    counter[dest]=(counter[dest][0]+1,counter[dest][1])
                else:
                    counter[dest]=(1,0)
        return counter
    print InOutCounter(Graphv)

if __name__ == "__main__":

    Graph = {}
    with open('data') as f:

        for val in f.readlines():
            val = val.strip().split()
            Graph[val[0]]=val[2].split(',')
    print Graph
    FindPath(Graph)
    #FindPath(Graph,edges,Path)
    '''
    result = list(nx.eulerian_circuit(G))
    output = str(result[0][0])
    for val in result:
        output+= '->{}'.format(val[1])
    print output
    with open('log.txt','w') as f:
        f.write(output)
    '''
