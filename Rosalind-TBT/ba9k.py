import sys
from itertools import cycle,islice
def FIRST_TO_LAST_ARRAY(text,location):
    lst=list(text)
    char = lst[location]
    indices = [i for i, x in enumerate(lst) if x == char]
    index = indices.index(location)
    srtdlst=list(text)
    srtdlst.sort()
    indices = [i for i, x in enumerate(srtdlst) if x == char]
    return indices[index]
if __name__ == "__main__":
    with open('data') as f:
        Text = f.readline().strip()
        location = int(f.readline().strip())
    res =FIRST_TO_LAST_ARRAY(Text,location)
    with open('log.txt','w') as f:
        f.write('{}'.format(res))
