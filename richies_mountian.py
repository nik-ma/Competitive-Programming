n=int(input())
num=[int(i) for i in input().split()]
dp=[[0 for i in range(n)] for i in range(n)]
for i in range(n):
    dp[i][0]='YES'
    
    flag=-1
    count=0
    for j in range(i+1,n):
        if num[j-1]<num[j] and flag!=2:
            flag=1
            dp[i][j]='YES'
        elif num[j-1]>num[j] and (flag==-1 or flag==2 or flag==1):
            flag=2
            dp[i][j]='YES'
        else:
            dp[i][j]='NO'
            break
q=int(input())
for i in range(q):
    l,r=map(int,input().split())
    print(dp[l-1][r-1])






