for _ in range(int(input())):
    n,d=map(int,input().split())
    num=[]
    for i in range(n):
        num.append(int(input()))
    num.sort()
    ways=0
    i=n-1
    while i>=1:
        if num[i]-num[i-1]<=d:
            ways+=1
            i-=2
        else:
            i-=1
    print(ways)
