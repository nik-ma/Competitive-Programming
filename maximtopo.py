# cook your dish here
from collections import Counter
import string
import math
import sys
sys.setrecursionlimit(10**6)
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
def dfs(node,parent):
    count=0
    global val
    for i in arr[node]:
        if i!=parent:
            count+=dfs(i,node)
    val[node-1]=count+1
    return count+1
testcases=vary(1)
fact=[1 for i in range(10**5+1)]
mod=10**9+7
for i in range(2,10**5+1):
    fact[i]=(fact[i-1]*i)%mod
for _ in range(testcases):
    n,kt=vary(2)
    arr=[[] for i in range(n+1)]
    vis=[0 for i in range(n+2)]
    for i in range(n-1):
        u,v=vary(2)
        arr[u].append(v)
        arr[v].append(u)

    ans=[]
    maxi=-1
    for i in range(n):
        maxi


        
    ans=sorted(ans,key=lambda x: (x[1]),reverse=True)
    # print(ans)
    ans.sort(reverse=True)
    # print(ans)
    print(ans[kt-1][0],ans[kt-1][1])





