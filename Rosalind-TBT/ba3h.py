def Composition(Patterns):
    k = len(Patterns[0])
    out = ''
    return out

if __name__ == "__main__":
    with open('data') as f:
        K = int(f.readline().strip())
        kmers = [j.strip() for j in f.readlines()]
    ls = Composition(kmers)
    with open('log.txt','w') as f:
        f.write(ls)


