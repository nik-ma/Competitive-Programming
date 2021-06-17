from collections import Counter
import string
import bisect
#import random
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
testcases=1
for _ in range(testcases):
    s=input()
    characters=[]
    for i in string.ascii_lowercase:
        characters.append(i)
    maxi=-1
    for i in characters:
        st=i
        maxi=max(maxi,s.count(st))
        for j in characters:
            pt=st+j
            countf=counts=0
            for i in range(len(s)):
                if s[i]==pt[0]:
                    countf+=1
                elif s[i]==pt[1]:
                    counts+=1
                
                

    print(maxi)

