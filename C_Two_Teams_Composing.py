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
    num=array_int()
    ct=makedict(num)
    st=set(num)
    if len(st)>max(ct.values()):
        print(max(ct.values()))
    elif len(st)==max(ct.values()):
        print(len(st)-1)
    else:
        print(len(st))