def ReconstructString(lst):
    out = lst[0]
    k = len(lst[0])
    for j in range(1,len(lst)):
        out+=lst[j][k-1]
    return out

if __name__ == "__main__":
    with open('data') as f:
        dna_lst = map(lambda x: x.strip(),f.readlines())
    ls = ReconstructString(dna_lst)
    print ls
    with open('log.txt','w') as f:
        f.write(ls)


