probs={}
with open('data') as f:
    ls = f.readlines()
    dnaxy = ls[0].strip().upper()
    dnaab = ls[4].strip()
    __,AX,AY,AZ = ls[9].split()
    __,BX,BY,BZ = ls[10].split()
    probs['AX']=float(AX)
    probs['AY']=float(AY)
    probs['AZ']=float(AZ)
    probs['BX']=float(BX)
    probs['BY']=float(BY)
    probs['BZ']=float(BZ)
total=1
for i in range(len(dnaxy)):
    total*=probs[dnaab[i]+dnaxy[i]]
print total
#    for i in probs.keys():
#        print i,probs[i],
#totalprob=0.5
#for i in range (len(dna)-1):
#    totalprob*= probs[dna[i:i+2]]
#print totalprob
