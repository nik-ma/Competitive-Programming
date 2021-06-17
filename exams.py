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
    n,k=vary(2)
    org,fake=[],[]
    org.append(n)
    fake.append(k)
    days=0
    for i in range(n):

        if fake[org.index(min(org))]==min(fake):
            days+=min(fake)
    