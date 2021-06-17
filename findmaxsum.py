def FindMaxSum(a, n):
    sum1=0
    sum2=0
    for i in range(0,n,2):
        sum1+=a[i]
    for i in range(1,n,2):
        sum2+=a[i]
    return max(sum1,sum2)
a=[int(x) for x in input().split()]
print(FindMaxSum(a,len(a)))

