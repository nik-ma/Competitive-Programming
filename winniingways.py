import operator as op
from functools import reduce

def ncr(n, r):
    r = min(r, n-r)
    numer = reduce(op.mul, range(n, n-r, -1), 1)
    denom = reduce(op.mul, range(1, r+1), 1)
    return numer //denom
for _ in range(int(input())):
    n=int(input())
    a=[int(i) for i in input().split()]
    q=int(input())
    for i in range(q):
        anew=[]
        l,r=map(int,input().split())
        for i in range(l-1,r):
            anew.append(a[i])
        b=set(anew)
        z=len(b)
        if z==1:
            move=1
            
        if z==len(anew):
            if z%2: 
                move=z
                
            else:
                move=0
                
        if z!=len(anew):
            if z%2:
                move=z
            else:
                c=0
                for i in b:
                    if anew.count(i)>1:
                        for k in range(1,anew.count(i)):
                            c+=ncr(anew.count(i),k)
                move=c
        print(move)
            

            