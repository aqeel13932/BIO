from itertools import permutations
from ba4c import GENERATE_THEORETICAL_SPECTRUM
values={'G':57,'A':71,'S':87,'P':97,'V':99,'T':101,'C':103,'I':113,'N':114,'D':115,'K':128,'E':129,'M':131,'H':137,'F':147,'R':156,'Y':163,'W':186}

def SCORE(pep,spec):
    actualspec = GENERATE_THEORETICAL_SPECTRUM(pep)
    actualspec.sort()
    score=0
    diction = {}
    for i in actualspec:
        diction[i]= diction.get(i,0) +1
    for j in diction:
        score+= min(spec.count(j),diction[j])
    return score

if __name__ == "__main__":
    with open('data') as f:
        pep = f.readline().strip()
        spec = map(int,f.readline().strip().split())
    #print res
    res=SCORE(pep,spec)
    print res
    with open('log.txt','w') as f:
        f.write('{}'.format(res))
