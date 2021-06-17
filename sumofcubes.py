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
    n=vary(1)
    # print(pow(n,1/3))
    # print((703657519796-5779**3)**(1/3))

    # print(5779**3+7993**3)
    for b in range(1,10000+2):
        # print(b)
        if (n-b**3)<=0:
            print('NO')
            break
        else:
            if math.ceil(math.pow(n-b**3,1/3))==math.floor(math.pow(n-b**3,1/3)):
                print('YES')
                break