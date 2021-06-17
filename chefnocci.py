for _ in range(int(input())):
    x,k=map(int,input().split())
    chefn=[]
    first=1
    second=2
    chefn.append(first)
    chefn.append(second)
    third=first+second
    while third<=1000000000:
        third=first+second
        chefn.append(third)
        first=second
        second=third
    print(chefn,len(chefn))
         