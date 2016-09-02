probs={}
with open('data') as f:
    ls = f.readlines()
    dna = ls[0].strip()
    __,AA,AB = ls[5].split()
    __,BA,BB = ls[6].split()
    probs['AA']= float(AA)
    probs['AB']= float(AB)
    probs['BA']= float(BA)
    probs['BB']= float(BB)

totalprob=0.5
for i in range (len(dna)-1):
    totalprob*= probs[dna[i:i+2]]
print totalprob
