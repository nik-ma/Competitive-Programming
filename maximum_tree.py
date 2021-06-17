for _ in range(int(input())):
    n=int(input())
    graph=[[0 for i in range(n+1)] for j in range(n+1)]
    for i in range(n-1):
        u,v=map(int,input().split())
        graph[u]=v
        graph[v]=u
    m=int(input())
    kot=[int(x) for x in input().split()]
    k=1
    for i in kot:
        k*=i
    def dfs(node,parent):
        