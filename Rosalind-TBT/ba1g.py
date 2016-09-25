with open('data') as f:
    data1 = f.readline().strip()
    data2 = f.readline().strip()

total = abs(len(data1)-len(data2))
counter = min(len(data1),len(data2))
for i in range (counter):
    total+= (data1[i]!=data2[i])
print total
