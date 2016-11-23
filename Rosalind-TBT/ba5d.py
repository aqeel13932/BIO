import sys
import networkx as nx
def COST(path,diction):
    total=0
    for i in range(len(path)-1):
        total+= diction[(path[i],path[i+1])]
    return total
    
if __name__ == "__main__":
    with open('data') as f:
        strt =int( f.readline().strip())
        end = int(f.readline().strip())
        lst = []
        for x in f.readlines():
            x = x.strip()
            x = x.split('->')
            t1,t2 = x[1].split(':')
            lst.append((x[0],t1,t2))
    Graph = nx.MultiDiGraph()
    diction = {}
    for node in lst:
        diction[node[0],node[1]]=int(node[2])
        Graph.add_edge(node[0],node[1])
    paths= nx.all_simple_paths(Graph,str(strt),str(end))
    
    maxp =0
    maxl =0
    for path in paths:
        cost = COST(path,diction)
        if cost>maxl:
            maxp = path
            maxl = cost
    res =  '->'.join(path)
    with open('log.txt','w') as f:
        f.write('{}\n{}'.format(maxl,res))
