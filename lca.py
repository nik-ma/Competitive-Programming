def lca(a,b):
    if level[a]<level[b]:
        level[a],level[b]=level[b],level[a]
        a,b=b,a
    diff=level[a]-level[b]
    while diff>0:
        a=parent[a]
        diff-=1
    if a==b:
        return a
    while parent[a]!=parent[b]:
        a,b=parent[a],parent[b]
    # print(a,b,parent[a],parent[b])
    return parent[a]

def defing_lca(node,lvl,par):
    level[node]=lvl     
    parent[node]=par
    for i in tree[node]:
        # print(i)
        if i!=par:
            defing_lca(i,lvl+1,node)
for t in range(int(input())):  
    n=int(input())
    level=[0]*(n+1)
    parent=[-1]*(n+1)
    tree=[[] for i in range(n+1)]
    for i in range(n):
        values=[int(i) for i in input().split()]
        # print(values)
        for j in range(values[0]):
            tree[i+1].append(values[j+1])

    defing_lca(1,0,1)
    # print(level)
    # print(parent)
    q=int(input())
    print('Case '+str(t+1)+':')
    for i in range(q):
        a,b=map(int,input().split())
        print(lca(a,b))
