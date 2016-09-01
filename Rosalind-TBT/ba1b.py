import collections
with open ('data') as f:
    code = f.readline().strip()
    k = int(f.readline().strip())
def kmermost(k,dna):
    diction={}
    for i in range(len(dna)-k):
        s= dna[i:i+k]
        if s in diction.keys():
            diction[s]+=1
        else:
            diction[s]=1
    diction =collections.OrderedDict(sorted(diction.items(),key=lambda t:t[1],reverse=True))
    top = diction[diction.keys()[0]]
    for i in diction.keys():
        if diction[i]==top:
            print i,
kmermost(k,code)

