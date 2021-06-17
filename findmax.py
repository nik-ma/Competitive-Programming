for _ in range(int(input())):
    n,k=map(int,input().split())
    num=[int(x) for x in input().split()]
    d=max(num)
    for i in range(n):
        num[i]=d-num[i]
    num2=num[:]
    d=max(num)
    for i in range(n):
        num2[i]=d-num2[i]
    if k==1:
        print(*num)
        continue
    if k==2:
        print(*num2)
        continue
    if k%2!=0:
        print(*num)
    else:
        print(*num2)