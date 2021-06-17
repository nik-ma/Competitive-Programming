
for _ in range(int(input())):
    ti=int(input())
    
    
    a=[int(x) for x in input().split()]
    b=[]
    for i in a:
        for j in a:
            binx=bin(i)[2:]
            biny=bin(j)[2:]
            binxpy=binx+biny
            binypx=biny+binx
            b.append(int(binxpy,2)-int(binypx,2))

    print(max(b))
        