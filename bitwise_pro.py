for _ in range(int(input())):
    x,y,l,r=map(int,input().split())
    for i in range(l,r+1):
        f=(x&i)*(y&i)
        print(i,f)
        
