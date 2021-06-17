from collections import Counter
import string
import math
import sys
# sys.setrecursionlimit(10**6) 
def array_int():
    return [int(i) for i in sys.stdin.readline().split()]
def vary(number_of_variables):
    if number_of_variables==1:
        return int(sys.stdin.readline())
    if number_of_variables>=2:
        return map(int,sys.stdin.readline().split()) 
def makedict(var):
    return dict(Counter(var))
for _ in range(vary(1)):
    n,k=vary(2)
    num=array_int()
    count=1
    kt=0
    for i in range(n-1):
        if num[i]<k:
            break
        else:
            num[i+1]+=num[i]-k
            kt=i+1
            count+=1
    count+=num[kt]//k
    print(count)
    