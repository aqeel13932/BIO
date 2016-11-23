import sys
import numpy as np

def LongestPath( Graph, source, sink):
    S_a={}
    for a in Graph:
        S_a{

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
    print lst
    res =0
    with open('log.txt','w') as f:
        f.write('{} '.format(res))
