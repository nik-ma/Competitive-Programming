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
    ct=[]
    count=0
    mini=9999999
    
    for i in range(n):
        initial=num[i]
        count=0
        back=initial
        for j in range(i-1,-1,-1):
            if num[j]>initial:
                count+=1
                if back<=num[j]:
                    back=num[j]
            
        for k in range(i+1,n):
            if mini>num[k]:
                mini=num[k]
            if back>num[k]:
                count+=1
        for v in range(i-1,-1,-1):
            if mini<num[v] and num[v]<=initial:
                count+=1
        ct.append(count)
    print(min(ct)+1,max(ct)+1)