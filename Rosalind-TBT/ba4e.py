from itertools import permutations
from ba4c import GENERATE_THEORETICAL_SPECTRUM
values={'G':57,'A':71,'S':87,'P':97,'V':99,'T':101,'C':103,'I':113,'N':114,'D':115,'K':128,'E':129,'M':131,'H':137,'F':147,'R':156,'Y':163,'W':186}
def GET_TOTAL(peptidestr):
    total = 0
    for l in peptidestr:
        total+=values[l]
    return total

def CONSISTANT(pep,PEPVALS):
    if GET_TOTAL(pep) not in PEPVALS:
        return False
    for i in range(1,len(pep)):
        for j in range(len(pep)-i+1):
            if GET_TOTAL(pep[j:j+i]) in PEPVALS:
                continue
            else:
                return False
    return True

def LIST_IN_LIST(pep,PEPVALS):
    therom = GENERATE_THEORETICAL_SPECTRUM(pep)
    for j in therom:
        if j in PEPVALS:
            continue
        else:
            print j
            return False
    return True

def TRIM(PEPTIDES,PEPVALS):
    nlst =[]
    for pep in PEPTIDES:
        if CONSISTANT(pep,PEPVALS):
        #if LIST_IN_LIST(pep,PEPVALS):
            nlst.append(pep)
    nlst = set(nlst)
    nlst = list(nlst)
    return nlst
def EXPAND(lst,base):
    expand =[]
    for i in range(len(lst)):
        for v in base:
            expand.append(lst[i]+v)
    return expand

def FIND_CYCLYIC_PEPTIDE(PEPVALS):
    for i in range(len(PEPVALS)):
        if sum(PEPVALS[:i])==PEPVALS[-1]:
            break
    baseline = []
    for v in values:
        if values[v] in PEPVALS:
            baseline.append(v)
    expand = EXPAND(baseline,baseline)
    trimed = TRIM(expand,PEPVALS)
    while len(trimed[0])!=(i-1):
        print len(trimed[0]),(i-1)
        expand = EXPAND(trimed,baseline)
        trimed=TRIM(expand,PEPVALS)
    return trimed
def PEPTIDE_TO_NUMBER(pep):
    return '-'.join(map(lambda x:str(values[x]),pep))
if __name__ == "__main__":
    
    with open('data') as f:
        pepvals = map(int,f.readline().strip().split())
    res = FIND_CYCLYIC_PEPTIDE(pepvals)
    res = map(PEPTIDE_TO_NUMBER,res)
    #print res
    with open('log.txt','w') as f:
        for i in res:
            f.write('{} '.format(i))
