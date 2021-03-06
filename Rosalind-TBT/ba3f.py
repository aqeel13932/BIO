import networkx as nx

if __name__ == "__main__":
    with open('data') as f:
        G = nx.DiGraph()
        for val in f.readlines():
            val = val.strip().split()
            for j in val[2].split(','):
                G.add_edge(val[0],j)
    result = list(nx.eulerian_circuit(G))
    output = str(result[0][0])
    for val in result:
        output+= '->{}'.format(val[1])
    print output
    with open('log.txt','w') as f:
        f.write(output)

