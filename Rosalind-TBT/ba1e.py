with open ('data') as f:
    data= f.readline().strip()
    k,l,t = map(int,f.readline().strip().split())
    print data,len(data)
print k,l,t
kmers={}
first=True
def findkmers(curdata):
    global kmers
    
    tmp = {}
    for j in range(len(curdata)-k+1):
        val = curdata[j:j+k]
        if val in tmp.keys():
            tmp[val]+=1
        else:
            tmp[val]=1
    for val in tmp.keys():
        if tmp[val]>= t:
            kmers[val] = tmp[val]
    
for i in range(len(data)-l+1):
    findkmers(data[i:i+l])#,len(data[i:i+l]
    first=False

print ' '.join( kmers.keys())
