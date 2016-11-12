from itertools import permutations
from ba4f import SCORE
from ba4e import PEPTIDE_TO_NUMBER
values={'G':57,'A':71,'S':87,'P':97,'V':99,'T':101,'C':103,'I':113,'L':113,'N':114,'D':115,'K':128,'Q':128,'E':129,'M':131,'H':137,'F':147,'R':156,'Y':163,'W':186}
def LinearSPectrum(Peptide):
    prefixmass={}
    prefixmass[-1]=0
    for i in range(len(Peptide)):
        for v in values:
            if v== Peptide[i]:
                prefixmass[i]= prefixmass[i-1]+values[v]
    LinearSpectrum =[]
    LinearSpectrum.append(0)
    for i in range(-1,len(Peptide)):
        for j in range(i+1,len(Peptide)):
            LinearSpectrum.append(prefixmass[j]-prefixmass[i])
    LinearSpectrum.sort()
    return LinearSpectrum

if __name__ == "__main__":
    with open('data') as f:
        pip = f.readline().strip()
    res = LinearSPectrum(pip)

    #res = LeaderboardCyclopeptideSequencing(pepvals,top)
    #res = PEPTIDE_TO_NUMBER(res[0])
    #print res
    #print res
    with open('log.txt','w') as f:
        for i in res:
            f.write('{} '.format(i))
