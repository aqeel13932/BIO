import sys
import networkx
from ba9a import TRIECONSTRUCTION,GET_NODE
def PREFIXTRIEMATCHING(Text,Trie):
    markstart=-10
    startnode=(0,'0')
    for i in range(len(Text)):
        newnode = GET_NODE(Text[i],Trie.neighbors(startnode))
        if newnode[0]>-1:
            if markstart==-10:
                markstart=newnode[0]
            startnode=newnode
            if (-1,'$') in Trie.neighbors(newnode):
                return markstart
        else:
            return -1
    return -1
def TRIEMATCHING(Text,Trie):
    allout=[]
    for i in range(len(Text)):
        out = PREFIXTRIEMATCHING(Text[i:],Trie)
        if out>-1:
            allout.append(str(i))
    return allout
if __name__ == "__main__":
    with open('data') as f:
        Text = f.readline().strip()
        lst = [s.strip() for s in f.readlines()]
    Trie = TRIECONSTRUCTION(lst)[1]
    res = TRIEMATCHING(Text,Trie)
    res= map(str,res)
    with open('log.txt','w') as f:
        f.write('{}'.format(' '.join(res)))
