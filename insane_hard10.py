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
for _ in range(int(input())):
    n,c,k=map(int,input().split())
    lisc=[0 for i in range(n)]
    slope=[[] for i in range(n)]
    for i in range(n):
        a,b,lisc[i]=map(int,input().split())
        slope[lisc[i]-1].append(a)
    v=[int(x) for x in input().split()]
    counter=dict(Counter(lisc))
    print(slope)