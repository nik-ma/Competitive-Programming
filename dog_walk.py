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
n,k=vary(2)
count=0
num=array_int()
for i in range(n-1):
    z=k-(num[i]+num[i+1])
    if z<=0:
        continue
    else:
        count+=z
        num[i+1]+=z
print(count)
print(*num)



