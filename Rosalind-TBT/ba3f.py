def EULERIANCYCLE(graph):
    pass

if __name__ == "__main__":
    with open('data') as f:
        graph = {}
        for val in f.readlines():
            val = val.strip().split()
            graph[val[0]] = map(int,val[2].split(','))

    print graph
    '''
    ls.sort()
    print '\n'.join(ls)
    with open('log.txt','w') as f:
        f.write('\n'.join(ls))
    '''

