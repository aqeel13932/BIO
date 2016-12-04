import sys
def rindex(mylist, myvalue):
        return len(mylist) - mylist[::-1].index(myvalue) - 1

def FIRST_TO_LAST_ARRAY(lst,srtdlst,location):
    char = lst[location]
    indices = [i for i, x in enumerate(lst) if x == char]
    index = indices.index(location)
    indices = [i for i, x in enumerate(srtdlst) if x == char]
    return indices[index]

def BWMATCHING(FirstColumn,LastColumn,Pattern,themap):
    top=0
    bottom=len(LastColumn)-1
    while top<= bottom:
        if len(Pattern)>0:
            symbol = Pattern[-1]
            Pattern=Pattern[:-1]
            if symbol in LastColumn[top:bottom+1]:
                topindex =LastColumn[top:bottom+1].index(symbol)+top
                bottomindex= rindex(LastColumn[top:bottom+1],symbol)+top
                top =FIRST_TO_LAST_ARRAY(LastColumn,FirstColumn,topindex)
                bottom=FIRST_TO_LAST_ARRAY(LastColumn,FirstColumn,bottomindex)
                tmp = bottom-top
            else:
                return 0
        else:
            return bottom-top+1
if __name__ == "__main__":
    with open('data') as f:
        Text = f.readline().strip()
        patterns = f.readline().strip().split(' ')
    frscol = list(Text)
    frscol.sort()
    lstcol = list(Text)
    themap ={}
    for i in range(len(lstcol)):
        themap[i]=FIRST_TO_LAST_ARRAY(lstcol,frscol,i)
    res =[]
    for pattern in patterns:
        res.append( BWMATCHING(frscol,lstcol,pattern,themap))
    res = map(str,res)
    with open('log.txt','w') as f:
        f.write('{}'.format(' '.join(res)))
