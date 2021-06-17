for _ in range(int(input())):
    n=int(input())
    weigth=[int(i) for i in input().split()]
    graph=[[]*(n+1)]*(n+1)
    for i in range(n-1):
        u,v=map(int,input().split())
        graph[u].append(v)        
        graph[v].append(u)
    def dfs(node,parent):
        