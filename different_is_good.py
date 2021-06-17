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
s=input()
st=makedict(list(s))
count=0
pt=0

for i in st:
    if st[i]>1:
        count+=st[i]-1
    pt+=1
if count==0:
    print(0)
else:
    if pt>=26:
        print(-1)
    else:

        if 1:
            if count>(26-pt):
                print(-1)
            else:
                print(count)
