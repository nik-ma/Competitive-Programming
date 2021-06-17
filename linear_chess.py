for _ in range(int(input())):
    n,k=map(int,input().split())
    num=[int(x) for x in input().split()]
    lis=[]
    lis2=[]
    for i in num:
        if k%i==0:
            lis.append(k//i)
            lis2.append(i)

    if len(lis)!=0:
        print(lis2[lis.index(min(lis))])
    else:
        print(-1)
