def Overlap(Patterns):
    out =[]
    lookup = {}
    for pat in Patterns:
        lookup[pat[:-1]]=pat
    for pat in Patterns:
        if pat[1:] in lookup.keys():
            out.append('{} -> {}'.format(pat,lookup[pat[1:]]))
    return out

if __name__ == "__main__":
    with open('data') as f:
        dna_lst = map(lambda x: x.strip(),f.readlines())

    ls = Overlap(dna_lst)
    ls.sort()
    print '\n'.join(ls)
    with open('log.txt','w') as f:
        f.write('\n'.join(ls))


