for i in range(int(input())):
    n=int(input())
    a=[int(x) for x in input().split()]
    c=0
    for i in range(n):
        for j in range(i+1,n):
            if (a[i]+a[j])%2!=0:
                c+=1
    print(c)