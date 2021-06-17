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
    n,k,x,y=vary(4)
    s=set()
    s.add(x)
    while 1:
        x=(x+k)%n
        if x in s:
            break
        else:
            s.add(x)
    if y in s:
        print('YES')
    else:
        print('NO')
    

