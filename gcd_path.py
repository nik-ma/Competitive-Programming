import math
def dfs(node,edges,k,val):
    global count
    global visited
    visited[node]=1
    if val[node]%k!=0:
        return
    count+=1
    # print(count)
    for i in edges[node]:
        if visited[i]==1:
            continue
        elif val[i]%k==0:
            # count+=1
            dfs(i,edges,k,val)
        elif val[node]%k!=0:
            return
def countPairs(n,edges,val,k):
    global count 
    global visited
    ans=0
    for i in range(n):
        count=0
        dfs(i,edges,k,val)
        # print(count)
        ans+=(count*(count-1))//2
    return ans
for _ in range(int(input())):
    n,k=map(int,input().split())
    val=[int(i) for i in input().split()]
    tree=[[] for i in range(n)]
    count=0
    visited=[0]*(n+1)
    for _ in range(n-1):
        x,y=map(int,input().split())
        tree[x].append(y)
        tree[y].append(x)
    print(countPairs(n,tree,val,k))

