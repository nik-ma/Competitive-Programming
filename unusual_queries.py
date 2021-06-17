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
n,q,s=vary(3)
num=array_int()
dp=[[-1 for i in range(n)] for j in range(n)]
values=[0 for i in range(n)]
for i in range(n):
    st=set()
    st.add(num[i])
    count=1
    maxi=num[i]
    for j in range(i,n):
        if num[j] in st:
            
            pass
        elif num[j]>maxi:
            maxi=max(num[j],maxi)
            count+=1
            st.add(num[j])
        dp[i][j]=count
    # values[i]=count
# print(dp)
# exit()
maximum=0
for _ in range(q):
    x,y=vary(2)
    l=(x+s*maximum-1)%n+1
    r=(y+s*maximum-1)%n+1
    if l>r:
        l,r=r,l
    maximum=-1
    for i in range(l-1,r):
        maximum=max(dp[i][r-1],maximum)
    print(maximum)    
    



