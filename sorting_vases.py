# cook your dish here
for _ in range(int(input())):
    n,m=map(int,input().split())
    l=[int(x) for x in input().split()]
    count=0
    a=[]
    for i in range(m):
        x,y=map(int,input().split())
        a.append([x,y])
    for i in range(n):
        while l[i]!=i+1:
            z=l[i]
            for j in range(m):
                if z==a[j][0] and l[z-1]==a[j][1]:
                    l[i],l[z-1]=l[z-1],l[i]
                    break
            else:
                l[i],l[z-1]=l[z-1],l[i]
                count+=1
    print(count)