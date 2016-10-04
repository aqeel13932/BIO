def EULERIANCYCLE(graph):
    pass

if __name__ == "__main__":
    with open('data') as f:
        kmers = [j.strip() for j in f.readlines()]
        print kmers
    ls = DeBruijn(kmers)
    ls.sort()
    print '\n'.join(ls)
    with open('log.txt','w') as f:
        f.write('\n'.join(ls))


