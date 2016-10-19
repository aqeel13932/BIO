import itertools

if __name__ == "__main__":
    with open('data') as f:
        k = int(f.readline().strip())
    lst = itertools.product(['0','1'],repeat=k)

    for i in lst:
        print i
    '''
    result = list(nx.eulerian_circuit(G))
    output = str(result[0][0])
    for val in result:
        output+= '->{}'.format(val[1])
    print output
    with open('log.txt','w') as f:
        f.write(output)
    '''
