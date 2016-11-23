import sys
import networkx as nx
def COST(path,diction):
    total=0
    for i in range(len(path)-1):
        total+= diction[(path[i],path[i+1])]
    return total
    
if __name__ == "__main__":
    with open('data') as f:
        ls = map(lambda x: x.strip().split(' -> '),f.readlines())
    Graph = nx.MultiDiGraph()
    for edge in ls:
        for end in edge[1].split(','):
            Graph.add_edge(edge[0],end)
    path = nx.topological_sort(Graph)
    res = ', '.join(path)
    print res
    with open('log.txt','w') as f:
        f.write('{}'.format(res))
