for _ in range(int(input())):
    n,m,c=map(int,input().split())
    upper=0
    lower=0
    for i in range(n):
        a,b=map(int,input().split())
        if b-m*a-c>0:
            upper+=1
        elif b-m*a-c<0:
            lower+=1
    print(lower*upper)
