import operator
with open('data') as f:
    data = f.readline().strip()

c=0
g=0
ls={}
for i in range(len(data)):
    if data[i]=='G':
        g+=1
    if data[i]=='C':
        c+=1
    ls[i+1]=g-c

sorted_words = sorted(ls.items(), key=operator.itemgetter(1),reverse=False)
basic =0
for i in range(len(sorted_words)):
    if i==0:
        print sorted_words[i][0],
        basic=sorted_words[i][0]
    elif sorted_words[i][1]==sorted_words[i-1][1]:
        print sorted_words[i][0],
    else:
        break
print ''
