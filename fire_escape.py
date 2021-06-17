global count
count=0
def dfs(node):
    global count
    visited[node]=1
    count+=1
    for i in arr[node]:
        if visited[i]==0:
            dfs(i)

for _ in range(int(input())):
    n,k=map(int,input().split())
    arr=[[] for i in range(n+1)]
    visited=[0]*(n+1)
    for i in range(k):
        x,y=map(int,input().split())
        arr[x].append(y)
        arr[y].append(x)
    concount=0
    res=1
    for i in range(1,n+1):
        
        if visited[i]==0:
            count=0
            dfs(i)
            concount+=1
            res=(res*count)%1000000007
    print(concount,res)
        
