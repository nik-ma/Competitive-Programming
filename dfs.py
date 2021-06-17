n,k=map(int,input().split())
arr=[[] for i in range(n+1)]
vis=[0 for i in range(n+2)]
count=0
def dfs(node):
    vis[node]=1
    for i in arr[node]:
        if vis[i]==0:
            dfs(i)


for i in range(k):
    x,y=map(int,input().split())
    arr[x].append(y)
    arr[y].append(x)
for i in range(1,n+1):
    if vis[i]==0:
        dfs(i)
        count+=1
print(count,arr)
