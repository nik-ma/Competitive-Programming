from collections import Counter
import string
import math
import sys
# sys.setrecursionlimit(10**6) 
from fractions import Fraction
def array_int():
    return [int(i) for i in sys.stdin.readline().split()]
def vary(arrber_of_variables):
    if arrber_of_variables==1:
        return int(sys.stdin.readline())
    if arrber_of_variables>=2:
        return map(int,sys.stdin.readline().split()) 
def makedict(var):
    return dict(Counter(var))
testcases=vary(1)
for _ in range(testcases):
    n,m=vary(2)
    john=array_int()
    opposition=array_int()
    john.sort()
    opposition.sort()
    count=0
    for i in range(min(n,m)):
        if sum(john)>sum(opposition):
            print(count)
            break
        else:
            john[i],opposition[m-i-1]=opposition[m-i-1],john[i]
            count+=1
    else:
        if sum(john)>sum(opposition):
            print(count)
        else:
            print(-1)
            

