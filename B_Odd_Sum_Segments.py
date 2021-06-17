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
    if k>n:
        print('NO')
    else:
        count=0
        for i in range(n):
            if num[i]%2!=0:
                count+=1
        if count<k or count%2!=k%2:
            print('NO')
        else:
            print('YES')
            for i in range(n):
                if num[i]%2!=0 and k>1:
                    print(i+1,end=" ")
                    k-=1
            print(n)
                

            