from collections import Counter
import string
import math
import sys
from bisect import bisect_left,bisect_right
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
for _ in range(testcases):
    n=vary(1)
    num=sorted(array_int())
    for i in range(vary(1)):
        coins=vary(1)
        print(bisect_right(num,coins,0,n))