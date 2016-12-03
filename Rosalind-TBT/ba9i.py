import sys
from itertools import cycle,islice
def BURROWS_WHEELER(text):
    lst=[]
    for i in range(len(text)):
        txt = cycle(text)
        lst.append(''.join(islice(txt,i,i+len(text))))
    lst.sort()
    indx=len(text)-1
    return ''.join([elm[indx] for elm in lst])
if __name__ == "__main__":
    with open('data') as f:
        Text = f.readline().strip()
    res = BURROWS_WHEELER(Text)
    with open('log.txt','w') as f:
        f.write('{}'.format(''.join(res)))
