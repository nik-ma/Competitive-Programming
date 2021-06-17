for _ in range(int(input())):
    n,k=map(int,input().split())
    if k<=n:
        print(k)
    else:
        if k%n==0:
            qu=k//n
            if qu%2==0:
                print(1+qu%n)
            
        