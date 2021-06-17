# cook your dish here
from collections import Counter
import string
import math
def array_int():
    return [int(i) for i in input().split()]
def variables(number_of_variables):
    if number_of_variables==1:
        return int(input())
    if number_of_variables>=2:
        return map(int,input().split()) 
def makedict(var):
    return dict(Counter(var))
mod=1000000007
def tofindmax(arr,n,k,tt):
    count=0
    for j in range(n):
            if count>=k:
                return tt
            else:
                count+=num[j]//tt
    if count<k:
        return 0
    else:
        return tt
for _ in range(int(input())):
    n,k=variables(2)
    num=array_int()
    s=sum(num)
    titu=s//k
    count=0
    low=1
    last=titu
    find=[]
    while low<=last:
        mid=(low+last)//2
        zz=tofindmax(num,n,k,mid)
        if zz>0:
            find.append(zz)
            low=mid
            last=last
        else:
            low=low
            last=mid
    print(max(find))

    
            
    
        
    
