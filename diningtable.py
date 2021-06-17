from collections import Counter
import string
import math
import bisect
# import random
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
    n=vary(1)
    num=array_int()
    mini=-10**10
    for i in range(n):
        value=[num[i]]
        for j in range(i+1,n):
            value.append(num[j])
            sumt=sum(value)
            c=0
            for k in range(n):
                for t in range(k+1,n):
                    if num[k:t+1]==value:
                        c+=1
            
            mini=max(mini,sumt*c)
    print(mini)

