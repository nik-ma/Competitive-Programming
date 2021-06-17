for _ in range(int(input())):
    p,m=map(int,input().split())
    if p<=m:
        print(0)
    else:
        print(p-m)
 