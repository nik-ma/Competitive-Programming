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
num=array_int()
n=num[0]
num=num[1:]
ans=0
i=0
j=n-1
s=0
while i<j:
    # print('eh')
    while j>i:
        if num[i]<num[j]:
            ans=max(ans,num[j]-num[i])
            # print(ans)
        j-=1
    s+=ans
    j=n-1
    i+=1
print(s)


                