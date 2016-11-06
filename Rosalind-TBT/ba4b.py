def reversedna (dna):
	diction={'A':'T','T':'A','C':'G','G':'C'}
	data = list(dna)
	data.reverse() 
	#print data
	output = ''.join(map(lambda x: diction[x],data))
	return output

def RNA_TO_AMINO(rna):
    x = {"UUU":"F", "UUC":"F", "UUA":"L", "UUG":"L",
        "UCU":"S", "UCC":"S", "UCA":"S", "UCG":"S",
        "UAU":"Y", "UAC":"Y", "UAA":"STOP", "UAG":"STOP",
        "UGU":"C", "UGC":"C", "UGA":"STOP", "UGG":"W",
        "CUU":"L", "CUC":"L", "CUA":"L", "CUG":"L",
        "CCU":"P", "CCC":"P", "CCA":"P", "CCG":"P",
        "CAU":"H", "CAC":"H", "CAA":"Q", "CAG":"Q",
        "CGU":"R", "CGC":"R", "CGA":"R", "CGG":"R",
        "AUU":"I", "AUC":"I", "AUA":"I", "AUG":"M",
        "ACU":"T", "ACC":"T", "ACA":"T", "ACG":"T",
        "AAU":"N", "AAC":"N", "AAA":"K", "AAG":"K",
        "AGU":"S", "AGC":"S", "AGA":"R", "AGG":"R",
        "GUU":"V", "GUC":"V", "GUA":"V", "GUG":"V",
        "GCU":"A", "GCC":"A", "GCA":"A", "GCG":"A",
        "GAU":"D", "GAC":"D", "GAA":"E", "GAG":"E",
        "GGU":"G", "GGC":"G", "GGA":"G", "GGG":"G",}
    AMINO=''
    for i in range(0,len(rna),3):
        val=x[rna[i:i+3]]
        if val=='STOP':
            continue
        AMINO+=val
    return AMINO
def SPECIFIC_MATCH(dna,target):
    size = len(target)*3
    output=[]
    for i in range(len(rna)-size+1):
        r= dna[i:i+size].replace('T','U')
        rr = reversedna(dna[i:i+size]).replace('T','U')
        #print r,RNA_TO_AMINO(r),rr,RNA_TO_AMINO(rr)
        if RNA_TO_AMINO(r)==target:
            output.append(dna[i:i+size])
        if RNA_TO_AMINO(rr)==target:
            output.append(dna[i:i+size])
       
    return output
    
if __name__ == "__main__":
    
    with open('data') as f:
        rna= f.readline().strip()
        target = f.readline().strip()
    res = SPECIFIC_MATCH(rna,target)
    res = map(lambda x: x.replace('U','T'),res)
    #res.sort()
    print res
    with open('log.txt','w') as f:
        for r in res : 
            f.write('{}\n'.format(r))
