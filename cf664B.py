n,m,x,y=map(int,input().split())
s=set()
s.add((x,y))
print(x,y)
if (x,1) in s:
    pass
else:
    s.add((x,1))
    print(x,1)
if (1,1) in s:
    pass
else:
    s.add((1,1))
    print(1,1)

for i in range(1,n+1):
    if i%2!=0:
        for j in range(1,m+1):
            if (i,j) in s:
                continue
            else:
                print(i,j)
                s.add((i,j))
    else:
        for j in range(m,0,-1):
            if (i,j) in s:
                continue
            else:
                print(i,j)
                s.add((i,j))
        
        
        