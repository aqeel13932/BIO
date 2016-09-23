probs={}
with open('data') as f:
    ls = f.readlines()
    dna = ls[0].strip().upper()
    probs['AA'],probs['AB']=map(float, ls[7].split()[1:])
    probs['BA'],probs['BB'] = map(float,ls[8].split()[1:])
    probs['AX'],probs['AY'],probs['AZ'] = map(float,ls[11].split()[1:])
    probs['BX'],probs['BY'],probs['BZ'] = map(float,ls[12].split()[1:])

for i in probs.keys():
    print i,probs[i]
