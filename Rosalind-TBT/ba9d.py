import sys
def LONGESTREPEAT(TEXT):
    k = len(TEXT)-1
    lenth = len(TEXT)
    Found=False
    while k>0:
        repeated={}

        for i in range(lenth-k+1):
            tmp = TEXT[i:i+k]
            repeated[tmp]=repeated.get(tmp,0)+1
            if repeated[tmp]>1:
                return tmp
        k-=1


    return result

if __name__ == "__main__":
    with open('data') as f:
        text = f.readline().strip()
    res = LONGESTREPEAT(text)
    with open('log.txt','w') as f:
        f.write('{}'.format(res))
