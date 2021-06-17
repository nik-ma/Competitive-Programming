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
    s=input()
    tt=''
    tt2=''
    k=1
    tt3=''
    value={}
    j=1
    for i in string.ascii_uppercase:
        value[i]=j
        j+=1
    print(value)
    for i in s:
        if i.isalpha():
            if k==2:
                k=3
                
                continue
            tt+=i
        else:
            if k==3:
                tt3+=i
            else:
                k=2
                tt2+=i
    if tt=='R':
        ans=''
        for i in tt2:
            ans+=value[i]
         


    
        


