def DeBruijn(Patterns):
    out=[]
    lookup={}
    for val in Patterns:
        if val[:-1] in lookup.keys():
            lookup[val[:-1]].append(val[1:])
        else:
            lookup[val[:-1]] = [val[1:]]


    for key in lookup.keys():
        out.append('{} -> {}'.format(key,','.join(lookup[key])))
    return out

if __name__ == "__main__":
    with open('data') as f:
        kmers = [j.strip() for j in f.readlines()]
        print kmers
    ls = DeBruijn(kmers)
    ls.sort()
    print '\n'.join(ls)
    with open('log.txt','w') as f:
        f.write('\n'.join(ls))


