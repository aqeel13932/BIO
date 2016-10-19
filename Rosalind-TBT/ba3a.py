def Composition(text,k):
    ls=[]
    for i in range(len(text)-k+1):
        ls.append(text[i:i+k])
    ls.sort()
    return ls

if __name__ == "__main__":
    with open('data') as f:
        k = int(f.readline().strip())
        dna = f.readline().strip()
    ls = Composition(dna,k)
    with open('log.txt','w') as f:
        f.write('\n'.join(ls))


