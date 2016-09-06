probs={}
with open('data') as f:
    ls = f.readlines()
    dna = ls[0].strip().upper()
    probs['AA'],probs['AB']=map(float, ls[7].split()[1:])
    probs['BA'],probs['BB'] = map(float,ls[8].split()[1:])
    probs['AX'],probs['AY'],probs['AZ'] = map(float,ls[11].split()[1:])
    probs['BX'],probs['BY'],probs['BZ'] = map(float,ls[12].split()[1:])

way={}
way[0]= (probs['A'+dna[0]],None,probs['B'+dna[0]],None)
for i in range(1,len(dna)):
    #Current A , Previous A
    AA = way[i-1][0]*probs['A'+dna[i]]*probs['AA']
    #Current A , Previous B
    AB = way[i-1][2]*probs['A'+dna[i]]*probs['AB']
    #Current B, Previous A
    BA = way[i-1][0]*probs['B'+dna[i]]*probs['BA']
    #Current B, Previous B
    BB = way[i-1][2]*probs['B'+dna[i]]*probs['BB']
    Afather = 'A' if AA>AB else 'B'
    Bfather = 'A' if BA>BB else 'B'
    way[i]=(max(AA,AB),Afather,max(BA,BB),Bfather)
output = []
#(Act as there is another element at the end where it's father is the max(A,B) of the final elementin the list)
Father ='A' if way[len(dna)-1][0]>way[len(dna)-1][2] else 'B'
for i in range(len(dna)-1,-1,-1):
    if Father =='A':
        #Register my self since I am the father.
        output.append('A')
        Father= way[i][1]
    elif Father =='B':
        #Register my self since I am the father.
        output.append('B')
        Father=way[i][3]
    else:
        break
output.reverse()
print "".join(output)
