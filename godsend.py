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
print(int('33',4)+int('32',4))

n=vary(1)
num=array_int()
cout=makedict(num)

count=0
for i in range(n):
    if num[i]%2==0:
        continue
    else:
        print('First')
        break
else:
    print('Second')
"""for i in cout:
    if i%2!=0:
        count+=cout[i]
if (count%2==0 and count!=0) or sum(num)%2!=0:
    print('First')
else:
    print('Second')"""
