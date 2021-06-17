from collections import Counter
import operator as op
from functools import reduce
def ncr(n, r):
    if n<r:
        return 0
    r = min(r, n-r)
    numer = reduce(op.mul, range(n, n-r, -1), 1)
    denom = reduce(op.mul, range(1, r+1), 1)
    return numer // denom  
def maxit(counter,erase,erase_l):
    maxin=-1
    flag=0
    for i in counter:
        if erase[i-1]!=0:
            k=erase_l//counter[i]
            if k!=0:
                if counter[i]>=3:
                    z1=(counter[i]*(counter[i]-1)*(counter[i]-2))
                else:
                    z1=0
                if counter[i]-k>=3:
                    z2=(counter[i]-k)*(counter[i]-k-1)*(counter[i]-k-2)
                else:
                    z2=0
                zo=(z1-z2)//6P
            else:
                continue
        else:
            continue
        if maxin<zo and erase_l>=erase[i-1]:
            flag=1
            maxin=zo
            p=i
        elif maxin<zo and erase_l<erase[i-1]:
            continue
    if flag!=1:
        return -1
    else:
        return p        
for _ in range(int(input())):
    n,c,k=map(int,input().split())
    lisc=[0 for i in range(n)]
    for i in range(n):
        a,b,lisc[i]=map(int,input().split())
    v=[int(x) for x in input().split()]
    counter=dict(Counter(lisc))
    #print(counter)
    maxi=-1
    if 1:
        for i in range(len(v)):
            if v[i]==0:
                counter[i+1]=0
    if k==0:
        ans=0
        for i in counter:
            ans+=ncr(counter[i],3)
        print(ans)
        continue
    while k>0:
        z=maxit(counter,v,k)
        if z==-1:
            break
        counter[z]-=1
        k-=v[z-1]
    ans=0
    for i in counter:
        ans+=ncr(counter[i],3)
    print(ans)
