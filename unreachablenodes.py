nodes,edges=map(int,input().split())
arr=[[] for i in range(nodes+1)]
visited=[0 for i in range(nodes+1)]
for i in range(edges):
    x,y=map(int,input().split())
    arr[x].append(y)
    arr[y].append(x)
xn=int(input())
def dfs(node):
    visited[node]=1
    for i in arr[node]:
        if visited[i]==0:
            dfs(i)
dfs(xn)
print(nodes-visited.count(1))