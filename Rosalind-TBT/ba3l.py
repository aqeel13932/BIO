from collections import defaultdict

if __name__ == "__main__":

    Graph = {}
    with open('data') as f:
        k,d =map(int, f.readline().strip().split())
        str1=''
        str2=''
        str1,str2 = f.readline().strip().split('|')
        for line in f.readlines():
            fst ,snd = line.strip().split('|')
            str1+=str(fst[-1])
            str2+=str(snd[-1])
    str1+=str2[-(k+d):]
    with open('log.txt','w') as f:
        f.write(str1)
