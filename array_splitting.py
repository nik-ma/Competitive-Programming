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
for _ in range(1):
    n,k=vary(2)
    num=array_int()
    num.sort(reverse=True)
    for i in range(n):
        if k==0:
            break
        if num[i]==num[i+1]:
            continue
        else:
            k-=1
    