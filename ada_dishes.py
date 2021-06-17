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
    n=vary(1)
    num=array_int()
    if n==1:
        print(num[0])
        continue
    if n==2:
        print(max(num))
        continue
    if n==3:
        num.sort()
        print(num[2]+num[2]-num[1])
    if n==4:
        num.sort()
        if num[1]+num[2]>num[3]:
            print(max(num[1]+num[2],num[3]+num[0]))
        else:
            print(max(num[3],num[2]+num[0]+num[1]))



