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
    global weight,graph,ans,timer,flat_tree,terminate,start,ind
    start[node]=timer
    flat_tree[ind]=node
    ind+=1
    timer+=1
    for i in graph[node]:
        if i!=parent:
            dfs(i,node)
    terminate[node]=timer
    flat_tree[ind]=node
    ind+=1
    timer+=1
n,q=vary(2)
weight=[99]+array_int()
graph=[[] for i in range(n+1)]
timer=1
start=[0 for i in range(n+1)]
terminate=[0 for i in range(n+1)]
flat_tree=[0 for i in range(2*n+1)]
for i in range(n-1):
    u,v=vary(2)
    graph[u].append(v)
    graph[v].append(u)
#print(graph)
ans=[[] for i in range(n+1)]
ind=1
dfs(1,-1)
print(flat_tree,start,terminate)
# print(ans) 
mod=2**32
queries=[]
for _ in range(q):
    u,v=vary(2)
    queries.append([u,v])
for j in queries:
    st=set()
    st.add(1)
    st.add(j[0])
    

