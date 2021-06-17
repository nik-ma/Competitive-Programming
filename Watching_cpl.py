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
    num.sort(reverse=True)
    towerA=towerB=0
    countA=countB=0
    i=0
    flagA=flagB=0
    while i<n:
        if towerA<k:
            towerA+=num[i]
            countA+=1
            if towerB<k and i<n-1:
                towerB+=num[i+1]
                countB+=1
                i+=2
                continue
            i+=1
        else:
            if towerB<k:
                towerB+=num[i]
                countB+=1
            i+=1
    # print(countB+countA)

        
    # print(num)
    # print(towerB,towerA)
    if towerA>=k and towerB>=k:
        print((countB+countA))
    else:
        print(-1)