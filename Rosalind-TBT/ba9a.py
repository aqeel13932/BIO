import sys
import networkx
def GET_NODE(char,neighbors):
    for elm in neighbors:
        if char==elm[1]:
            return elm
    return -1,-1
def TRIECONSTRUCTION(Patterns):
    graph = networkx.DiGraph()
    rank=0
    linkslst=[]
    graph.add_node((rank,'0'))
    for pat in Patterns:
        startnode = (0,'0')
        current =''
        pmax = len(pat)
        for i in range(pmax):
            out = GET_NODE(pat[i],graph.neighbors(startnode))
            if out[0]>-1:
                #current=':'.join([str(out[0]),out[1]])
                current=str(out[0])
                startnode=out
            else:
                if i==0:
                    current+='0'
                rank+=1
                graph.add_edge(startnode,(rank,pat[i]))
                startnode = (rank,pat[i])
                if i<(pmax-1):
                    current+='->{}:{}\n{}'.format(str(rank),pat[i],str(rank))
                else:
                    current+='->{}:{}'.format(str(rank),pat[i])
        graph.add_edge(startnode,(-1,'$'))
        linkslst.append(current)
    return linkslst,graph

if __name__ == "__main__":
    with open('data') as f:
        lst = [s.strip() for s in f.readlines()]
    res = TRIECONSTRUCTION(lst)[0]
    res= map(str,res)
    with open('log.txt','w') as f:
        f.write('{}'.format('\n'.join(res)))
