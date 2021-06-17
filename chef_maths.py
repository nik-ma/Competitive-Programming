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
mod=1000000007
for _ in range(vary(1)):
    n=vary(1)
    num=array_int()
    num.sort()
    ans=-10**20
    if num[0]>=0:
        print(num[n-1]*num[n-2]*num[n-3]*num[n-4]*num[n-5])
    else:
        ans=max(ans,num[0]*num[1]*num[2]*num[3]*num[n-1])
        ans=max(ans,num[n-1]*num[n-2]*num[n-3]*num[0]*num[1])
        print(max(ans,num[n-1]*num[n-2]*num[n-3]*num[n-4]*num[n-5]))



    



