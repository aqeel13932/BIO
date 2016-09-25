with open('data') as f:
   val = f.readline().strip()
   data = f.readline().strip()
   d = int(f.readline().strip())
def space(data1,data2):
    total = abs(len(data1)-len(data2))
    counter = min(len(data1),len(data2))
    for i in range (counter):
        total+= (data1[i]!=data2[i])
    return total
length = len(val)
output=[]
for i in range(len(data)-length+1):
    if space(data[i:i+length],val)<=d:
        output.append(str(i))
print ' '.join(output)
