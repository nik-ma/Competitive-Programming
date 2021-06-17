n=int(input())
num=[int(x) for x in input().split()]
num.sort(reverse=True)
q=int(input())
""" for i in range(q):
    k=int(input())
    sum=0
    for i in range(k):
        sum+=num[i]
    print(sum)
 """

sum_num=sum(num)
dp=[0]*(n+1)
dp[0]=sum_num
for i in range(1,n):
    dp[i]=dp[i-1]-num[i-1]
q=int(input())
for i in range(q):
    k=int(input())
    print(dp[k])


