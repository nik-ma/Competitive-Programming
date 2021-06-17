import string
import math
from collections import Counter
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
n=vary(1)
num=array_int()
#print(num)
num.sort()
#print(num)
count=0
for i in range(n):
    for j in range(i+1,n):
        if num[i]==num[j]:
            num[j]+=1
            count+=1


    
#print(num)
print(count)
    