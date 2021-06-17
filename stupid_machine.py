

    
for _ in range(int(input())):
    n=int(input())
    lis=list(int(i) for i in input().split())
    token=0
    k=0
    while len(lis)>0:
        k=min(lis)
        token+=k*len(lis)
        for i in range(len(lis)):
            lis[i]-=k
        lis=lis[:lis.index(0)]
    print(token)
