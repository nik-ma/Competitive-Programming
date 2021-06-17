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
    n,k=vary(2)
    s=list(input())
    for i in range(k):
        value=s[i]
        for j in range(i+k,n,k):
            if s[j]!='?':
                if value=='?':
                    value=s[j]
                    break
        for j in range(i,n,k):
            if s[j]=='?':
                s[j]=value
    # print(s)
    ones=s[:k].count('1')
    zeros=s[:k].count('0')
    ques=s[:k].count('?')
    # print(ones,zeros,ques)
    flag=0
    if ones==zeros:
        if ques%2==0:
            flag=1 
        else:
            flag=0
    else:
        if (ques-(max(ones,zeros)-min(ones,zeros)))>=0 and (ques-(max(ones,zeros)-min(ones,zeros)))%2==0:
            flag=1
        else:
            flag=0
    if flag==0:
        print('NO')
    else:
        flag=0
        for i in range(k):
            if flag==1:
                break
            value=s[i]
            for j in range(i+k,n,k):
                if value!=s[j]:
                    # print('NO')
                    flag=1
                    break
        if flag==0:
            print('YES')
        else:
            print('NO')