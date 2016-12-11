import numpy as np
def VETERBI(O,S,SO,TM,EM,IP):
    T1=np.zeros((len(S),len(SO)))
    T2=np.zeros(T1.shape,dtype=int)
    T1[:,0] = IP*EM[:,O[SO[0]]]
    for i in range(1,len(SO)):
        for j in range(len(S)):
            T1[j,i]= np.max(T1[:,i-1]*TM[:,j]*EM[j,O[SO[i]]])#,axis=0)
            T2[j,i]= np.argmax(T1[:,i-1]*TM[:,j]*EM[j,O[SO[i]]])
    ZT = np.argmax(T1,axis=0)
    XT = [S[i] for i in ZT]
    for i in range(T1.shape[1]-1,0,-1):
        ZT[i-1]=T2[ZT[i],i]
        XT[i-1]=S[ZT[i-1]]
    return XT

if __name__ == "__main__":
    with open('data') as f:
        string = f.readline().strip().upper()
        f.readline()
        alphabet = f.readline().strip().upper().split()
        alphabet = {alphabet[i]:i for i in range(len(alphabet))}
        f.readline()
        states= f.readline().strip().upper().split()
        #states= {states[i]:i for i in range(len(states))}
        f.readline()
        f.readline()
        transitionMatrix=np.zeros((len(states),len(states)))
        for i in range(len(states)):
            transitionMatrix[i,:] = [float(i) for i in f.readline().strip().split()[1:]]
        f.readline()
        f.readline()
        emissionmatrix=np.zeros((len(states),len(alphabet)))
        for i in range(len(states)):
            emissionmatrix[i,:] = [float(i) for i in f.readline().strip().split()[1:]]
        #initialProb=[1/len(states)]*len(states)
        
        initialProb=[1]*len(states)
    res = VETERBI(alphabet,states,string,transitionMatrix,emissionmatrix,initialProb)
    with open('log.txt','w') as f:
        f.write(''.join(res))

