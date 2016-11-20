import sys
def DPChange(money,coins):
    MinNumCoins={0:0}
    for m in range (1,money+1):
        MinNumCoins[m]= sys.maxint
        for v in coins:
            if m>=v:
                if MinNumCoins.get(m-v,sys.maxint)+1< MinNumCoins[m]:
                    MinNumCoins[m]=MinNumCoins.get(m-v,sys.maxint)+1
    return MinNumCoins[money]
if __name__ == "__main__":
    with open('data') as f:
        money = int(f.readline().strip())
        coins = map(int,f.readline().split(','))
    coins.sort()
    res = DPChange(money,coins)
    print res
    with open('log.txt','w') as f:
        f.write('{} '.format(res))
