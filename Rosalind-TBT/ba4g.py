from itertools import permutations
from ba4f import SCORE
from ba4e import PEPTIDE_TO_NUMBER
values={'G':57,'A':71,'S':87,'P':97,'V':99,'T':101,'C':103,'I':113,'N':114,'D':115,'K':128,'E':129,'M':131,'H':137,'F':147,'R':156,'Y':163,'W':186}

def CUT(PEPTIDES,PEPVALS,N):
    nlst =[]
    for pep in PEPTIDES:
        nlst.append((pep,SCORE(pep,PEPVALS)))
    
    nlst.sort(key=lambda tup:tup[1],reverse=True)
    output=[]
    finished = False
    for j in range(min(N,len(nlst))):
        chk = nlst[j][1]
        output.append(nlst[j][0])
        if j==(N-1):
            while True:
                if len(nlst)<N:
                    break
                if nlst[j][1]!=nlst[j+1][1]:
                    break
                else:
                    output.append(nlst[j][0])
                    j=j+1
    return output
def EXPAND(lst,base):
    expand =[]
    for i in range(len(lst)):
        for v in base:
            expand.append(lst[i]+v)
    return expand

def LeaderboardCyclopeptideSequencing(PEPVALS,N):
    for i in range(len(PEPVALS)):
        if sum(PEPVALS[:i])==PEPVALS[-1]:
            break
    baseline = []
    for v in values:
        if values[v] in PEPVALS:
            baseline.append(v)
    expand = EXPAND(baseline,baseline)
    trimed = CUT(expand,PEPVALS,N)
    while len(trimed[0])!=(i-1):
        print len(trimed[0]),(i-1)
        expand = EXPAND(trimed,baseline)
        trimed=CUT(expand,PEPVALS,N)
    return trimed
if __name__ == "__main__":
    
    with open('data') as f:
        top = int(f.readline().strip())
        pepvals = map(int,f.readline().strip().split())
    print top
    print pepvals
    res = LeaderboardCyclopeptideSequencing(pepvals,top)
    print res[0]
    res = PEPTIDE_TO_NUMBER(res[0])
    print res
    #print res
    with open('log.txt','w') as f:
        f.write('{}'.format(res))
