from itertools import cycle,islice
values={'G':57,'A':71,'S':87,'P':97,'V':99,'T':101,'C':103,'I':113,'L':113,'N':114,'D':115,'K':128,'Q':128,'E':129,'M':131,'H':137,'F':147,'R':156,'Y':163,'W':186}
def GET_TOTAL(peptidestr):
    total = 0
    for l in peptidestr:
        total+=values[l]
    return total

def GENERATE_THEORETICAL_SPECTRUM(peptide):
    peptides=[]
    values=[]
    for i in range (1,len(peptide)):
        for j in range(len(peptide)):
            c = cycle(peptide)
            val=list( islice(c,j,j+i))
            peptides.append(''.join(val))
            values.append(GET_TOTAL(val))
    peptides.append(peptide)
    values.append(GET_TOTAL(peptide))
    values.append(0)
    return values


if __name__ == "__main__":
    
    with open('data') as f:
        peptidecode= f.readline().strip()
    res = GET_TOTAL(peptidecode)
    res = GENERATE_THEORETICAL_SPECTRUM(peptidecode)
    res.sort()
    print GET_TOTAL('LN')
    print res
    with open('log.txt','w') as f:
        for i in res:
            f.write('{} '.format(i))
