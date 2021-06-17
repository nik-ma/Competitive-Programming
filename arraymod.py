tc=int(input())
l=[0 for i in range(tc)]
while tc:
    s=0
    n,m,q=map(int,input().split())
    p=[[0 for i in range(m)]for j in range(m)] 
    for i in range(q):
        c,d=map(int,input().split())
        for j in range(n):
            p[c-1][j]+=1
        for k in range(m):
            p[k][d-1]+=1
    for i in range(n):
        for j in range(m):
            if p[i][j]%2!=0:
                l[s]+=1
    s+=1
    tc-=1
for i in range(s):
    print(l[i])

