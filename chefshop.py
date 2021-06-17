for _ in range(int(input())):
    n=int(input())
    l=[]
    for i in range(n):
        s,p,v=map(int,input().split())
        z=(p//(s+1))*v
        l.append(z)
    print(max(l))
   