from collections import Counter
import string
import math
import sys
# sys.setrecursionlimit(10**6) 
from fractions import Fraction
def array_int():
    return [int(i) for i in sys.stdin.readline().split()]
def vary(arrber_of_variables):
    if arrber_of_variables==1:
        return int(sys.stdin.readline())
    if arrber_of_variables>=2:
        return map(int,sys.stdin.readline().split()) 
def makedict(var):
    return dict(Counter(var))
for _ in range(vary(1)):
    n,m=vary(2)
    num=array_int()
    z=set(num)
    pt=list(z)
    if m<len(set(num)):
        print(-1)
        continue
    elif m==len(set(num)):
        print(m*n)
        print(*(pt*n))
    else:
        print(m*n)
        for i in range(m-len(z)):
            pt.append(1)
        print(*(pt*n))
    