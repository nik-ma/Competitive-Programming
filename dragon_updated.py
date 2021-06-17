n,q=map(int,input().split())
h=[int(x) for x in input().split()]
a=[int(x) for x in input().split()]
for i in range(1,n+1):
    for j in range(i,n+1):
        if h[i]>h[j]:
            continue
        else:
            break
