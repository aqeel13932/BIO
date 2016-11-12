from itertools import permutations
from ba4j import LinearSPectrum
from ba4e import PEPTIDE_TO_NUMBER
values={'G':57,'A':71,'S':87,'P':97,'V':99,'T':101,'C':103,'I':113,'L':113,'N':114,'D':115,'K':128,'Q':128,'E':129,'M':131,'H':137,'F':147,'R':156,'Y':163,'W':186}

def SCORE(pep,spec):
    score=0
    diction = {}
    for i in actualspec:
        diction[i]= diction.get(i,0) +1
    for j in diction:
        score+= min(spec.count(j),diction[j])
    return score

def LinearScore(Peptide,spectrum):
    linspec= LinearSPectrum(Peptide)
    diction={}
    score=0
    for i in linspec:
        diction[i]= diction.get(i,0)+1
    for j in diction:
        score+=min(spec.count(j),diction[j])
    return score
if __name__ == "__main__":
    with open('data') as f:
        pip = f.readline().strip()
        spec = map(int,f.readline().strip().split())
    res = LinearScore(pip,spec)
    print res
    with open('log.txt','w') as f:
            f.write('{}'.format(res))
