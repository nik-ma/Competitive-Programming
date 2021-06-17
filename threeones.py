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
    s=list(input())
    ct=makedict(s)
    twos=ones=0
    for i in ct:
        twos+=ct[i]//2
        ones+=ct[i]%2
    print(min(twos,ones)+(twos-min(twos,ones))//3)
    

        


