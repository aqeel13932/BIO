with open('data') as f:
    data =(f.readline().strip())

dna = {'A':0 ,'C':1,'G':2,'T':3}
def PatternToNumbe(pattren):
#    print pattren
    if len(pattren)==0:
        return 0
    sym = pattren[len(pattren)-1]
    pref = pattren[:len(pattren)-1]
    return 4*PatternToNumbe(pref)+dna[sym]

print PatternToNumbe(data)


