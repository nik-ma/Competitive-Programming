for _ in range(int(input())):
    n,k=map(int,input().split())
    arr={}
    visited=[0]*(n+1)
    for i in range(k):
        a,b=map(int,input().split())
        if str(a) not in arr:
            arr[str(a)]=[b]
        else:
            arr[str(a)].append(b)
        if str(b) not in arr:
            arr[str(b)]=[a]
        else:
            arr[str(b)].append(a)
    count=0
    def dfs(node):
        visited[node]=1
        for i in arr[str(node)]:
            if visited[i]==0:
                dfs(i)
        return
            
    for i in range(n):
        if visited[i]==0:
            dfs(i)
            count+=1
    print(count)


    

