for _ in range(int(input())):
    n=([int(i) for i in input().split()])
    p = n[-1]
    sum=0
    for i in range(len(n)-1):
        sum+=n[i]*p
    if sum>120:
        print('Yes')
    else:
        print('NO')


