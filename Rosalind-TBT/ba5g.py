import sys
import numpy as np

def EDIT_DISTANCE(str1,l1,str2,l2):
    cost=0
    if (l1==0):
        return l2
    if (l2==0):
        return l1
    if str1[l1-1]!=str2[l2-1]:
        cost+=1
    return min(EDIT_DISTANCE(str1,l1 - 1, str2,l2 ) + 1,EDIT_DISTANCE(str1,l1    , str2, l2 - 1) + 1,EDIT_DISTANCE(str1,l1 - 1,str2,l2 - 1) + cost);

def EDIT_DISTANCE2(str1,str2):
    if str1==str2:
        return 0
    l1 = len(str1)
    l2 = len(str2)
    matrix = np.zeros((l1+1,l2+1))
    matrix[1:,0] = range(1,l1+1)
    matrix[0,1:] = range(1,l2+1)
    for j in range(1,l2+1):
        for i in range(1,l1+1):
            if str1[i-1]==str2[j-1]:
                substitutionCost=0
            else:
                substitutionCost=1
            matrix[i,j]= min(matrix[i-1,j]+1,matrix[i,j-1]+1,matrix[i-1,j-1]+substitutionCost)
    return int(matrix[l1,l2])
if __name__ == "__main__":
    with open('data') as f:
        w1 = f.readline().strip()
        w2 = f.readline().strip()
    #res = EDIT_DISTANCE(w1,len(w1),w2,len(w2))
    
    res = EDIT_DISTANCE2(w1,w2,)
    print res
    with open('log.txt','w') as f:
        f.write('{} '.format(res))
