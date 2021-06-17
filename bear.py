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
n,a=vary(2)
num=array_int()
z=min(a,n-a+1)
#print(z)
count=num.count(1)
#print(count)
for i in range(z):
    #print(num[a-1-i],num[a-1+i])
    if num[a-1-i]!=num[a-1+i]:
        
        
        count-=1
print(count)
        

