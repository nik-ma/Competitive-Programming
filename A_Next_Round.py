from collections import Counter
import string
import math
import sys
def printDivisors(n) : 
      
    # Note that this loop runs till square root 
    divisor=[]
    i = 1
    while i <= math.sqrt(n): 
          
        if (n % i == 0): 
              
            # If divisors are equal, print only one 
            if (n // i == i): 
                divisor.append(i) 
            else: 
                # Otherwise print both 
                divisor.extend((i,n//i)) 
        i = i + 1
    return divisor
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
# testcases=vary(1)
for _ in range(testcases):
    n,k=vary(2)
    num=array_int()
    ans=0
    for i in range(n):
        if num[i]>=num[k-1] and num[i]!=0:
            ans+=1
    print(ans)