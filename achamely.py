tc=int(input())
c=[0]*tc
while tc:
    
    n,h,y1,y2,l=map(int,input().split())
    while n:
        t,x=map(int,input().split(' '))
        if (t==2 and x<=h+y2) or (t==1 and h-y1<=x):
            n=n-1
            c[tc]=c[tc]+1
            continue
        elif l!=0:
            l=l-1
        n=n-1
    tc=tc-1
    print(c)

