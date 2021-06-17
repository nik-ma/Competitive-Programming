for _ in range(int(input())):
    n= int(input())
    a=[]
    i=1
    while i<=n*n:
        a.append([int(j) for j in range(i,i+n)])
        i+=n
    for i in range(len(a)):
        if i%2!=0:
            a[i].reverse()
        for j in range(n):
            print(a[i][j],end=" ")
        print()




            
    