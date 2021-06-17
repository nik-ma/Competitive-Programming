from collections import Counter
import string
import math
import sys
def array_int():
    return [int(i) for i in sys.stdin.readline().split()]
def vary(number_of_variables):
    if number_of_variables==1:
        return int(sys.stdin.readline())
    if number_of_variables>=2:
        return map(int,sys.stdin.readline().split()) 
def makedict(var):
    return dict(Counter(var))
mod=100000007
m,n=vary(2)
ans=0
if n%2==0:
    ans+=(n//2)*m
    
else:
    ans+=m*(n-1)//2
    if m%2==0:
        ans+=m//2
    else:
        ans+=(m-1)//2
print(ans)