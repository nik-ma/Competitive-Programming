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
    if n==1:
        num=array_int()
        pos=set()
        neg=set()
        for i in range(1,num[0]+1):
            if num[i]>0:
                pos.add(num[i])
            else:
                neg.add(num[i])
        print(len(pos)*len(neg))