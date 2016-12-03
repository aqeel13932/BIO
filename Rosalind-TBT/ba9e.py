import sys
def LONGESTSHARED(TEXT1,TEXT2):
    k = len(TEXT1)-1
    lenth = len(TEXT1)
    while k>0:
        t1=set()
        t2=set()
        for i in range(lenth-k+1):
            t1.add(TEXT1[i:i+k])
            t2.add(TEXT2[i:i+k])
        for n in t1.intersection(t2):
             return n
        k-=1


    return 'nono'

if __name__ == "__main__":
    with open('data') as f:
        text1 = f.readline().strip()
        text2 = f.readline().strip()
    res = LONGESTSHARED(text1,text2)
    print(res)
    with open('log.txt','w') as f:
        f.write('{}'.format(res))
