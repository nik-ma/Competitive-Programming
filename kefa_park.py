import collections,sys,threading
sys.setrecursionlimit(10**9)
threading.stack_size(10**8)
ans=0
def solve():
    def dfs(node,consecutive):
        global ans
        visited[node]=1
        if cats[node-1]==1:
            consecutive+=1
        else:
            consecutive=0
        if consecutive>m:
            return 0
        ok=1
        if 1:
            for i in tree[node]:
                if visited[i]==0:
                    ok=0
                    dfs(i,consecutive)
        if ok==1:
            ans+=1
        
    n,m=map(int,input().split())
    cats=list(map(int,input().split()))
    tree=[[] for i in range(n+1)]
    visited=[0]*(n+1)
    for _ in range(n-1):
        u,v=map(int,input().split())
        tree[u].append(v)
        tree[v].append(u)
    # ans=0
    dfs(1,0)
    print(ans)
threading.Thread(target=solve).start()
