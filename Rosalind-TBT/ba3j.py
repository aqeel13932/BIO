def OrderList(lst):
    dilst = {}
    ditmp={}
    for i in lst:
        dilst[i[:-1]]=(i,False)
        ditmp[i[1:]]=i
    print ditmp
    for i in lst:
        print i
        if i[:-1] in ditmp:
            print i, ditmp[i[:-1]]
        else:
            print 'not'
    exit()
    #Find Start
    for i in lst:
        if i[:-1] not in ditmp:
            print i
            exit()
    exit()
    print dilst
    startpoints=None
    for i in lst:

        count=0
        tmp = None
        print i

            #dilst[i[:-1]]=(i,True)

if __name__ == "__main__":

    Graph = {}
    with open('data') as f:
        k,d =map(int, f.readline().strip().split())
        str1ls=[]
        str2ls=[]
        for line in f.readlines():
            fst,snd = line.strip().split('|')
            str1ls.append(fst)
            str2ls.append(snd)

        OrderList(str1ls)
        exit()
        print str1,str2
    str1+=str2[-(k+d):]
    with open('log.txt','w') as f:
        f.write(str1)
