import sys
from itertools import cycle,islice
def INVERSEBURROWS_WHEELER(text):
    
    lst=list(text)
    srtdlst=list(text)
    for j in range(1,len(text)):
        srtdlst = sorted(srtdlst)
        srtdlst = [lst[i]+srtdlst[i] for i in range(len(lst))]
    for i in srtdlst:
        if i[-1]=='$':
            return i

    return 'non'
if __name__ == "__main__":
    with open('data') as f:
        Text = f.readline().strip()
    res =INVERSEBURROWS_WHEELER(Text)
    with open('log.txt','w') as f:
        f.write('{}'.format(''.join(res)))
