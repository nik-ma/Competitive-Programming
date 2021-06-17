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
    n=int(input())
    num=list(map(int,input().split()))
    ans=0
    for i in range(1,n):
        ans+=ncr(n-i,1)
    print(ans)
