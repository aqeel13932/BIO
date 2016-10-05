def Composition(Patterns):
    k = len(Patterns[0])
    out = ''
    lookup ={}
    #for val in Patterns:
    #    lookup
    while len(Patterns)>1:
        for i in range (len(Patterns)):
            if Patterns[0][-k+1:] == Patterns[i][:k-1]:
                Patterns[0]+= Patterns[i][k-1:]
                Patterns.remove(Patterns[i])
                break
        if len(Patterns)>1:
            for j in range (len(Patterns)):
                if Patterns[1][-k+1:] == Patterns[j][:k-1]:
                    Patterns[1]+= Patterns[j][k-1:]
                    Patterns.remove(Patterns[j])
                    break
    return Patterns[0]

if __name__ == "__main__":
    with open('data') as f:
        K = int(f.readline().strip())
        kmers = [j.strip() for j in f.readlines()]
    ls = Composition(kmers)
    print ls
    with open('log.txt','w') as f:
        f.write(ls)


