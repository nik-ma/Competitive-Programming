for i in range(int(input())):
    n,m=map(int,input().split())
    price=[-1]*m
    num=[int(x) for x in input().split()]
    marr=[int(x) for x in input().split()]
    j=0
    for i in num:
        if price[i-1]==-1:
            price[i-1]=marr[j]
        else:
            price[i-1]+=marr[j]
        j+=1
    price.sort()
    for i in range(m):
        if price[i]!=-1:
            print(price[i])
            break
            

        
