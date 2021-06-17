for _ in range(int(input())):
    n,k=map(int,input().split())
    price=[int(i) for i in input().split()]
    sum=0
    for i in price:
        if i>k:
            sum+=i-k
    print(sum)
