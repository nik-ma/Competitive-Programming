nodes,edges=map(int,input().split())
arr=[[] for i in range(nodes+1)]
timer_A=[0 for i in range(nodes+1)]
timer_B=[0 for i in range(nodes+1)]
global timer
timer=1

visited=[0 for i in range(nodes+1)]
for i in range(edges):
    x,y=map(int,input().split())
    arr[x].append(y)
    arr[y].append(x)
def dfs(node):
    global timer
    visited[node]=1
    timer_A[node]=timer
    timer+=1
    for i in arr[node]:
        if visited[i]==0:
            dfs(i)
        else:

            timer_B[node]=timer
            timer+=1


for i in range(1,nodes):
    if visited[i]==0:
        dfs(i)
print(timer_A,timer_B)



    
