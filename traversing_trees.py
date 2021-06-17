def dfs(node,parent):
    global graph, weight
    visited[node]=1
    for i in graph[node]:
        if i==parent:
            continue
        dfs(i,node)


for _ in range(int(input())):
    global graph,weight
    n,q=map(int,input().split())
    weight=list(map(int,input().split()))
    visited=[0]*(n+1)
    graph=[[0 for i in range(n+1)] for j in range(n+1)]
    
    for i in range(n):
        u,v=map(int,input().split())
        graph[u].append(v)
        graph[v].append(u)
    for i in range(1,n+1):
        dfs(i)
        
    
