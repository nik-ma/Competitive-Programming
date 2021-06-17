for i in range(int(input())):
    n=int(input())
    A=[int(x) for x in input().split()]
    B=[int(y) for y in input().split()]
    sum=0
    A.sort()
    B.sort()
    for i in range(n):
        if A[i]>=B[i]:
            sum+=B[i]
        else:
            sum+=A[i]
    print(sum)