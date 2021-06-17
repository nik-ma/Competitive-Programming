for _ in range(int(input())):
    n,l = map(int,input().split())
    a = [int(i) for i in input().split()]
    lis = [-1 for i in range(l)]
    sol = 0

    for i in range(n):
        var = i - lis[a[i] - 1] - 1
        if sol < var:
            sol = var

        lis[a[i]-1] = i

    for i in range(l):
        if sol < n -lis[i] -1:
            sol = n - lis[i] - 1 

    for i in range(l):
        if lis[i] == -1:
            sol = n
            break
    print(sol)