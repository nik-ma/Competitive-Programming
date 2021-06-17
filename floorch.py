for _ in range(int(input())):
    n,a,b,c=map(int,input().split())
    fl=list(map(int,input().split()))
    find=[]
    for i in range(n):
        find.append((abs(fl[i]-b)+c)+abs(fl[i]-a))
    print(min(find))