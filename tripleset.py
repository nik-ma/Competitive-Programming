import math
for _ in range(int(input())):
    a,b,c=map(int,input().split())
    p,q,r=map(int,input().split())
    if a==p and b==q and c==r:
        print(0)
        continue
    if p==0 and q==0 and r==0:
        print(1)
        continue
    if a==0 and b!=0 and c!=0:
        pass



    
    
    d1=p-a
    d2=q-b
    d3=r-c
    p1=math.floor(p/a)
    p2=math.floor(q/b)
    p3=math.floor(r/c)
    #for same difference or same ratio
    if ((p1==p/a and p2==q/b and p3==r/c)and (p1==p2 and p2==p3))or(d1==d2 and d2==d3):
        print(1)
        continue
    #for 1 zero and two equal or two zero
    if (d1==0 and (d1==d2 or d2==d3 or d3==d1)) or (d2==0 and (d1==d2 or d2==d3 or d3==d1)) or (d3==0 and (d1==d2 or d2==d3 or d3==d1)):
        print(1)
        continue
    #for 1 zero and other two have same ratio 
    if (d1==0 and ((p2==q/b and p3==r/c)and p2==p3))or(d2==0 and ((p1==p/a and p3==r/c)and p1==p3))or(d3==0 and ((p2==q/b and p1==p/a)and p1==p2)):
        print(1)
        continue
    #all difference are not equal and none of them is zero
    if ((d1!=d2 and d2!=d3 and d3!=d1)and (d1!=0 and d2!=0 and d3!=0)):
        #if ratio of any two are same
        if ((p1==p/a and p2==q/b)and(p1==p2))or((p2==p/a and p3==r/c)and(p2==p3))or((p3==r/c and p1==p/a)and(p1==p3)):
            print(2)
        else:
            m=min(p1,p2,p3)
            a1,b1,c1=m*a,m*b,m*c
            d11=p-a1
            d12=q-b1
            d13=r-c1
            #after multiplying with lowest quotiont none of differnce is same
            if d11!=d12 or d12!=d13 or d13!=d11:
                print(3)
            else:
                print(2)
    else:
        print(2)



     