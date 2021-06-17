from collections import Counter
import string
import math
def ncr(n , k): 
    global mod,fact
    num=fact[n]
    den=(fact[n-k]*fact[k])%mod
    return (num*pow(den,mod-2,mod))%mod
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
fact=[1]*100001
c=1
for i in range(1,100001):
    fact[i]=(c*i)%mod
    c=fact[i]
for _ in range(int(input())):
    n=vary(1)
    num=array_int()
    ans=0
    num.sort(reverse=True)
    count=0
    z=num[0]
    for i in range(n):
        if num[i]>=z:
            count+=1
    if count%2!=0:
        ans+=pow(2,n,mod)
    else:
        ans+=(pow(2,n))-ncr(count,count//2)*pow(2,n-count,mod)
    print(ans%mod)
    

