import sys
def SHORTESTNOTSHARED(TEXT1,TEXT2):
    k =1 
    lenth = len(TEXT1)
    while k<lenth:
        t1=set()
        t2=set()
        for i in range(lenth-k+1):
            t1.add(TEXT1[i:i+k])
            t2.add(TEXT2[i:i+k])
        result = t1.difference(t2)
        if len(result)>0:
            return result.pop()
        k+=1


    return ''

if __name__ == "__main__":
    with open('data') as f:
        text1 = f.readline().strip()
        text2 = f.readline().strip()
    res = SHORTESTNOTSHARED(text1,text2)
    print(res)
    with open('log.txt','w') as f:
        f.write('{}'.format(res))
