values={'G':57,'A':71,'S':87,'P':97,'V':99,'T':101,'C':103,'I':113,'L':113,'N':114,'D':115,'K':128,'Q':128,'E':129,'M':131,'H':137,'F':147,'R':156,'Y':163,'W':186}
val = set(values.values())
def PEPTIDE_COUNTER(M):
    AllPossibleCounts = {0:1}
    for i in range(M-57+1):
        j = i+57
        for v in val:
            if j-v in AllPossibleCounts:
                AllPossibleCounts[j] = AllPossibleCounts.get(j,0)+AllPossibleCounts[j-v]
    return AllPossibleCounts

    
if __name__ == "__main__":
    with open('data') as f:
        wantednumber = int(f.readline().strip())
    x= PEPTIDE_COUNTER(wantednumber)[wantednumber]
    print x
    with open('log.txt','w') as f:
        f.write('{}'.format(x))
