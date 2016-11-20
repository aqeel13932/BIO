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

if __name__ == "__main__":
    with open('data') as f:
        n,m = map(int,f.readline().strip().split())
        col =  map(lambda x: [int (r) for r in f.readline().strip().split()],range(n))
        f.readline()
        row = map(lambda x: [int (r) for r in  f.readline().strip().split()],range(n+1))
    res = MAX_LENGTH(col,row,(0,0),(n,m),n,m)
    with open('log.txt','w') as f:
        f.write('{} '.format(res))
