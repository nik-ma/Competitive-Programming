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

p=num[0]
num3=[]
for i in range(1,n):
    if p-num[i]<=0:
        num3.append(-1)
    else:
        num3.append(p-num[i])
k=0
count=0
#print(num3)
for i in range(n-2):
    if num3[i]>num3[i+1] and (k==0 or k==1):
        if k==0:
            tt=num3[i]
            k=1

        if num3[i+1]==-1:
            count+=tt
            continue
        
        
        continue
    if num3[i]<num3[i+1] and (k==0 or k==2):
        if num3[i]==-1:
            k=0
            continue
        else:
            count+=num3[i+1]
        k=2
        continue
print(count)

   
    
    

