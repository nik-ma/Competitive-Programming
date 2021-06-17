for _ in range(int(input())):
    p=int(input())
    m=[]
    n=[]
    for i in range(p):
        x,y=map(int,input().split())
        m.append(x)
        n.append(y)
    dx={}
    dy={}
    ans = p*(p-1)//2
    for i in m:
        if i in dx:
            dx[i]+=1
        else:
            dx[i]=1
    for i in n:
        if i in dy:
            dy[i]+=1
        else:
            dy[i]=1      
    for i in dx:
        temp = dx[i]
        ans -= temp*(temp -1)//2

    for i in dy:
        temp = dy[i]
        ans -= temp*(temp -1)//2
    print(ans)