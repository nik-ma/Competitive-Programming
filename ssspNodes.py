n=int(input())
arr=[[] for i in range(n+1)]
visited=[0 for i in range(n+1)]
dis=[0 for i in range(n+1)]
for i in range(n-1):
    x,y=map(int,input().split())
    arr[x].append(y)
    arr[y].append(x)

def dfs(node,dist):
    visited[node]=1
    dis[node]=dist
    for i in arr[node]:
        if visited[i]==0:
            dfs(i,dis[node]+1)
dfs(1,0)
min=10000000000
ans=0
for _ in range(int(input())):
    girl=int(input())
    if dis[girl]<min:
        min=dis[girl]
        ans=girl
    else:
        if dis[girl]>min and girl<ans:
            ans=girl

print(ans)