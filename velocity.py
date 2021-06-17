import math
for _ in range(int(input())):
    a,b,g=map(float,input().split())
    l,q=map(int,input().split())
    values=[]
    
    for i in range(q):
        x,d=map(int(input()))
        values.append([x,d])
    v=pow(2*a*values[0][1],2)
    values.append([0,l])
    t=pow((2*values[0][1])/a,2)
    
    for i in range(q):
        if values[0][i]==1:
            v=v**2-2*a*(values[0][i+1]-values[0][i])
            if v<0:
                print(-1)
                break
            else:
                t+=
                continue
        elif values[0][i]==2:
            v=v**2+2*a*(values[0][i+1]-values[0][i])


        

