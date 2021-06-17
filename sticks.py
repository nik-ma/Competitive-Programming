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
for _ in range(vary(1)):
    n=vary(1)
    num=array_int()
    count=makedict(num)
    kt=0
    for i in count:
        if i!=0:
            kt+=1
    print(kt)
