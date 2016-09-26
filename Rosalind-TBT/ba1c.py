with open('data') as f:
    data = f.readline().strip()
diction={'A':'T','T':'A','C':'G','G':'C'}
data = list(data)
data.reverse() 
#print data
output = ''.join(map(lambda x: diction[x],data))
print output
#print output.reverse()

