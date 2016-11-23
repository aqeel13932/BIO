import sys
import numpy as np


def MAX_LENGTH(col,row,strt,end,n,m):
    col = np.array(col)
    row = np.array(row)
    matrix = np.zeros((n+1,m+1))
    for i in range(n+1):
        for j in range(m+1):
            if (i==0):
                if j==0:
                    continue
                matrix[i,j]=sum(row[0,0:j])
                continue
            if (j==0):
                matrix[i,j]=sum(col[0:i,j])
                continue
            matrix[i,j]= max(matrix[i-1,j]+col[i-1,j],matrix[i,j-1]+row[i,j-1])
            
    return int(matrix[end])


def BUILD_COST_MAP(str1,str2):
    matrix = np.zeros((len(str1)+1,len(str2)+1))
    print len(str1),len(str2),matrix.shape
    for i in range(1,matrix.shape[0]):
        for j in range(1,matrix.shape[1]):
            matrix[i,j]=max(matrix[i-1,j],matrix[i,j-1],matrix[i-1,j-1]+ 1 if str1[i-1]==str2[j-1] else 0)
    return matrix


def LONGEST_PATH(matrix,str1,str2):
    output=[]
    current=(matrix.shape[0]-1,matrix.shape[1]-1)
    r = len(str1)
    c = len(str2)
    while (r>0 and c>0):
        if (matrix[r][c]-1) == matrix[r-1][c-1] and str1[r-1]==str2[c-1]:
            output = [str1[r-1]]+output
            r-=1
            c-=1
        elif matrix[r-1][c]>matrix[r][c-1]:
            r-=1
        else:
            c-=1
    return ''.join(output)


if __name__ == "__main__":
    with open('data') as f:
        col = list(f.readline().strip())
        row = list(f.readline().strip())
    res = BUILD_COST_MAP(col,row)
    print res
    res = LONGEST_PATH(res,col,row)
    with open('log.txt','w') as f:
        f.write('{} '.format(res))
