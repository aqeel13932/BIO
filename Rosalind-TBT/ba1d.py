with open ('data') as f:
    keyword = f.readline().strip()
    data = f.readline().strip()
length = len(keyword)
for i in range(len(data)-length-1):
    if keyword==data[i:i+length]:
        print i,
print ''
