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
testcases=vary(1)
for _ in range(testcases):
    n,k=vary(2)
    num=array_int()
    p=array_int()
    p.sort()
    tt=100
    while tt:
        for i in range(k):
            if num[p[i]]<num[p[i]-1]:
                num[p[i]],num[p[i]-1]=num[p[i]-1],num[p[i]]
        tt-=1
    # print(num)
    if sorted(num)==num:
        print('YES')
    else:
        print('NO')
        