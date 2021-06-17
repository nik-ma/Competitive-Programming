from collections import Counter
import string
import math
import bisect
#import random
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
def dfs(node,par):
    global count
    if tokens[node]==1:
        return
    for i in tree[node]:
        if i!=par:
            if tokens[i]==1:
                count+=1
                dfs(i,node)

for _ in range(testcases):
    n=vary(1)
    tree=[[] for i in range(n+1)]
    tokens=[0]+[int(i) for i in input()]
    par=array_int()
    for i in range(n-1):
        tree[par[i]].append(i+1)
        tree[i+1].append(par[i])
    ans=0
    for i in range(1,n+1):
        count=0
        dfs(i,i)
        ans+=count