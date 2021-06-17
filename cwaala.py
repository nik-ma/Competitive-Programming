from collections import Counter
import random
import string
import math
import bisect
# import random
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
def bfs(node,visited,fixed):
    level=[0]*(n+1)
    queue.append(node)
    level[node]=0
    visited.add(node)
    while len(queue)>0:
        value=queue.pop(0)
        
        for i in tree[value]:
            if i not in visited:
                level[i]=level[value]+1
                distance[fixed][i]=level[i]
                queue.append(i)
                visited.add(i)
        
        
testcases=vary(1)
for _ in range(testcases):
    n,q=vary(2)
    distance=[[0]*(n+1) for i in range(n+1)]
    tree=[[] for i in range(n+1)]
    for i in range(n-1):
        u,v=vary(2)
        tree[u].append(v)
        tree[v].append(u)
    
    for i in range(1,n+1):
        queue=[]
        visited=set()
        bfs(i,visited,i)
    # print(tree)
    # print(distance)
    for _ in range(q):
        a,b=vary(2)
        ans=0
        for i in range(1,n+1):
            # print(i,'=',getDist(i,a),getDist(i,b))

            ans+=min(distance[i][a],distance[i][b])
        print(ans)