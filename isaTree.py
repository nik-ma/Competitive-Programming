nodes,edges=map(int,input().split())
arr=[[] for i in range(nodes+1)]
visited=[0 for i in range(nodes+1)]
for i in range(edges):
    x,y=map(int,input().split())
    arr[x].append(y)
    arr[y].append(x)
def dfs(node):
    visited[node]=1
    for i in arr[node]:
        if visited[i]==0:
            dfs(i)
count=0
for i in range(1,nodes+1):
    if visited[i]==0:
        dfs(i)
        count+=1
if count<=1 and edges==nodes-1:
    print('YES')
else:
    print(count,'NO')
