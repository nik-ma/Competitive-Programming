# cook your dish here
import math
for _ in range(int(input())):
    n,m,x,y=map(int,input().split())
    if x>y and (n*m)%2==0:
        print(y*((n*m)//2))
        continue
    if x>y and (n*m)%2!=0:
        print(y*(((n*m)//2)+1))
        continue
    
    if (n*m)%2==0 and y-x<=x:
        print(x*((n*m)//2)+(y-x)*((n*m)//2))
    elif (n*m)%2!=0 and y-x<=x:
        print(x*((n*m)//2+1)+(y-x)*((n*m)//2))
    elif (n*m)%2==0 and y-x>x:
        print(x*((n*m)//2)+(x)*((n*m)//2))
    elif (n*m)%2!=0 and y-x>x:
        print(x*((n*m)//2)+(x)*((n*m)//2))


    