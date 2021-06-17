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
n,k=vary(2)
num=array_int()
tt=[0]*n
for i in range(k):
    l,r=vary(2)
    tt[l-1]+=1
    try:
        tt[r]-=1
    except:
        pass
for i in range(1,n):
    tt[i]+=tt[i-1]
tt.sort()
num.sort()
ans=0
for i in range(n):
    ans+=tt[i]*num[i]
print(ans)
    


    


    



