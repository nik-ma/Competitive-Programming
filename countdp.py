from collections import Counter
import string
import math
def array_int():
    return [int(i) for i in input().split()]
def vary(number_of_variables):
    if number_of_variables==1:
        return int(input())
    if number_of_variables>=2:
        return map(int,input().split()) 
def makedict(var):
    return dict(Counter(var))
mod=1000000007
if 1:
    n,q=vary(2)
    num=array_int()
    tt=set()
    dp=[0]*n
    dp[n-1]=1
    tt.add(num[n-1])
    for i in range(n-2,-1,-1):
        if num[i] in tt:
            dp[i]=dp[i+1]
            continue
        else:
            dp[i]=dp[i+1]+1
            tt.add(num[i])
        #print(tt)
    #print(num,dp)
    
    for i in range(q):
        ttt=vary(1)
        #print('ans')
        if ttt==1:
            print(dp[0])
            continue
        if ttt==n:
            print(1)
            continue
        print(dp[ttt-1])




    
