for i in range(int(input())):
    n,k=map(int,input().split())
    a=[int(i) for i in input().split()]
    l=[]
    for i in range(n):
        c=0
        for j in range(i,n):
            if a[i]==a[j]:
                c+=1
                continue
            else:
                l.append(c)
                break
        else:
            l.append(c)

    print(max(l))
    