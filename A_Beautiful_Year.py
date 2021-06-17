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
testcases=1
def check(n):
    s=set()
    z=n
    while n>0:
        s.add(n%10)
        n//=10
    if len(s)==len(str(z)):
        return 0
    else:
        return 1
for _ in range(testcases):
    n=vary(1)
    n+=1
    while check(n):
        n+=1
    print(n)
    