def Composition(Patterns):
    k = len(Patterns[0])

    out = ''
    lookup ={}
    for val in Patterns:
        lookup[val[:-1]]= val
    print lookup
    while len(lookup.keys())>1:
        for val in lookup.keys():
            if not val in lookup.keys():
                continue
            if lookup[val][-k+1:] in lookup.keys():
                tmps = lookup[lookup[val][-k+1:]][k-1:]
                lookup.pop(lookup[val][-k+1:],None)
                lookup[val] += tmps
    return lookup[lookup.keys()[0]]

if __name__ == "__main__":
    with open('data') as f:
        K = int(f.readline().strip())
        kmers = [j.strip() for j in f.readlines()]
    ls = Composition(kmers)
    print ls
    with open('log.txt','w') as f:
        f.write(ls)


