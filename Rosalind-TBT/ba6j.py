import sys
def Break2OnGenomeGraph(GenomGraph,i,i_,j,j_):
    try:
        GenomGraph.remove([i,i_])
    except:
        GenomGraph.remove([i_,i])

    try:
        GenomGraph.remove([j,j_])
    except:
        GenomGraph.remove([j_,j])
    GenomGraph.append([i,j])
    GenomGraph.append([i_,j_])
    return GenomGraph
if __name__ == "__main__":
    with open('data') as f:
        edges = f.readline().strip().split('), (')
        edges[0]=edges[0][1:]
        edges[-1]= edges[-1][:-1]
        edges = [map(int,i.split(',')) for i in edges]
        i, i_ ,j ,j_ =map(int,f.readline().strip().split(', '))
    res = Break2OnGenomeGraph(edges,i,i_,j,j_)
    res = map(lambda x: '({}, {})'.format(x[0],x[1]),res)


    with open('log.txt','w') as f:
        f.write('{}'.format(', '.join(res)))
