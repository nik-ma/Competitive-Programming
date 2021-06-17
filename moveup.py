for _ in range(int(input())):
    n=int(input())
    s=input()
    
    x,y=0,0
    b=list(s)
    l=[]
    for i in range(n):
        if b[i]!=b[i-1]  or i==0:
            l.append(b[i])
    for i in l:
        if i=="L":
            x-=1
        if i=="R":
            x+=1
        if i=="U":
            y+=1
        if i=="D":
            y-=1
    print(l)
    
    print(x,y)
            
