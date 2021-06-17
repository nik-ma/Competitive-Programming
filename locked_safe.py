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
    n=vary(1)
    num=array_int()+[19]
    if n==1:
        print(0)
        continue
    tt=1
    ans=[]
    for i in range(n):
        if num[i]!=num[i+1]:
            ans.append(tt)
            tt=1
        else:
            tt+=1
    total=0
    for i in ans:
        total+=(i*(i+1))//2
    print((n*(n+1))//2-total)


