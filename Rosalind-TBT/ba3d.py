def PathGraph(Text,K):
    kmers = []
    for i in range(len(Text)-K+1):
        kmers.append(Text[i:i+K])
    return kmers
def DeBruijn(Text,K):
    patterns = []
    patlen = K-1
    for i in range(len(Text)-patlen+1):
        patterns.append(Text[i:i+patlen])
    patterns = sorted(set(patterns))
    out =[]
    lookup = {}
    patcheck={}
    for pat in patterns:
        if pat in patcheck.keys():
            continue
        else:
            patcheck[pat]=True
        if pat[:-1] in lookup.keys():
            lookup[pat[:-1]].append(pat)
        else:
            lookup[pat[:-1]] = [pat]

    for pat in patterns:
        if pat[1:] in lookup.keys():
            out.append('{} -> {}'.format(pat,','.join(lookup[pat[1:]])))
    return out

if __name__ == "__main__":
    with open('data') as f:
        k =int(f.readline().strip())
        text = f.readline().strip()
    ls = DeBruijn(text,k)
    ls.sort()
    print '\n'.join(ls)
    with open('log.txt','w') as f:
        f.write('\n'.join(ls))


