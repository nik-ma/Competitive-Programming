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
    a,b,k=vary(3)
    boys=array_int()
    girls=array_int()
    if k<2:
        print(0)
        continue
    bct=makedict(boys)
    tob=sum(bct.values())
    gct=makedict(girls)
    tog=sum(gct.values())
    count=0
    for i in range(k):
        count+=min(tog-gct[girls[i]],tob-bct[boys[i]])
        tog-=1
        tob-=1
        gct[girls[i]]-=1
        bct[boys[i]]-=1
    print(count-1)








    