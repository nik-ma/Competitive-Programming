from collections import Counter
import string
import math
import sys
#sys.setrecursionlimit(10**6) 
def array_int():
    return [int(i) for i in sys.stdin.readline().split()]
def vary(number_of_variables):
    if number_of_variables==1:
        return int(sys.stdin.readline())
    if number_of_variables>=2:
        return map(int,sys.stdin.readline().split()) 
def makedict(var):
    return dict(Counter(var))
def countBits(number):
    return int((math.log(number)/math.log(2)) + 1)
for _ in range(vary(1)):
    n,x,p,k=vary(4)
    num=array_int()
    num.sort()
    ans=0
    if k>p:
        if num[p-1]<x:
            print(-1)
            continue
        if num[p-1]==x:
            print(0)
            continue
        ind=0
        for i in range(n):
            if num[i]>x:
                ind=i
                break
    
        ans=((p-1)-ind)+1
    if k<p:
        if num[p-1]>x:
            print(-1)
            continue
        if num[p-1]==x:
            print(0)
            continue
        ind=0
        for i in range(n):
            if num[i]<x:
                ind=i
        
        ans=(ind-(p-1))+1
    if k==p:
        if num[p-1]==x:
            print(0)
            continue
        if num[p-1]<x:
            ind=0
            for i in range(n):
                if num[i]<x:
                    ind=i
            
            ans=(ind-(p-1))+1
        elif num[p-1]>x:
            ind=0
            for i in range(n):
                if num[i]>x:
                    ind=i
                    break
        
            ans=((p-1)-ind)+1


    print(ans)

            
            

