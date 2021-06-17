def equilibriumPoint(A, N):
    sum1=0
    sum2=0
    for i in range(N-1):
        sum1+=A[i]

        sum2+=sum(A)-A[i+1]-sum1
        print(sum1,sum2)
        if sum1==sum2:
            print(A[i+1])
            break
        sum2=0
a=[int(x) for x in input().split()]
equilibriumPoint(a,len(a))