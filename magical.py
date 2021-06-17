for _ in range(int(input())):
    n,k=map(int,input().split())
    s=(k*(k+1))//2
    if n>k:
        print((k*(k+1))//2)
    else:
        if n==2:
            print(2)
            continue
        sk=s-2*(k-n+1)-((k-n+1)*(k-n+2)//2)+1
        print(sk)
     