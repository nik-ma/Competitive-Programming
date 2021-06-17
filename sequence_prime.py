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
n=vary(1)
if n==1:
    print(1)
elif n>1 and n<=10:
    for i in range(10,10+n,1):
        print(i,end=" ")
elif n>10 and n<=100:
    for i in range(100,100+n,1):
        print(i,end=" ")
elif n>100 and n<=1000:
    for i in range(1000,1000+n,1):
        print(i,end=" ")
elif n>1000 and n<=10000:
    for i in range(10000,10000+n,1):
        print(i,end=" ")
elif n>10000 and n<=100000:
    for i in range(100000,100000+n,1):
        print(i,end=" ")
elif n>100000 and n<=1000000:
    for i in range(1000000,1000000+n,1):
        print(i,end=" ")
else:
    pass

    

