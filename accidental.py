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
cubes=[i*i*i for i in range(1,10000+1)]
cb=set(cubes)
for _ in range(testcases):
    n=vary(1)
    for i in cb:
        if n-i in cb:
            print('YES')
            break
    else:
        print('NO')

