for _ in range(int(input())):
    n,x=map(int,input().split())
    a=list(map(int,input().split()))
    mod=998244353
    pro=a[0]**(n*(n+1))
    pre=0
    prod=1
    for i in range(n):
        pre=pre+x**i
        prod*=(pre**2)
    for i in range(n,0,-1):
        prod*=i
    print((prod*pro)%mod)




        
