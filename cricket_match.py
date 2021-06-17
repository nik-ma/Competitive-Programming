for _ in range(int(input())):
    p,m,n=map(int,input().split())
    if n%m!=0:
        print(n+2)
    else:
        x=n//m
        print((x-1)*m+2)
    
