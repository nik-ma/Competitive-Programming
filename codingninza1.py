for _ in range(int(input())):
    a,b=map(int,input().split())
    pro=a//b
    if pro!=0:
        print(0)
        continue
    x=1
    for i in range(1,a+1):
        x=x*i
        if x>=b:
            x%=b
    print(x)
    
        
    