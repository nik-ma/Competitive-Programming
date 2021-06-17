from collections import Counter
import string
import math
import sys

def array_int():
    return [int(i) for i in sys.stdin.readline().split()]
def vary(number_of_variables):
    if number_of_variables==1:
        return int(sys.stdin.readline())
    if number_of_variables>=2:
        return map(int,sys.stdin.readline().split()) 
def makedict(var):
    return dict(Counter(var))
mod=1000000007
a,b=vary(2)
q=vary(1)
ans=[]
for i in range(1,int(math.sqrt(1000000000))+1):
    if a%i==0 and b%i==0:
        ans.append(i)
ans.sort(reverse=True)
#print(ans)
for k in range(q):
    low,high=vary(2)
    flag=0
    for i in range(len(ans)):
        a=low
        b=high
        if flag==1:
            break
        while a<=b:
            mid=(a+b)//2
            if mid==ans[i]:
                print(mid)
                flag=1
                break
            if mid<ans[i]:
                a=mid+1
                
            if mid>ans[i]:
                b=mid-1
    else:
        print(-1)
            






