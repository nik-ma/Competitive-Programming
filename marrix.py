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
    arr=[]
    for i in range(n):
        arr.append(array_int())
    q=vary(1)
    for _ in range(q):
        x,y,v=vary(3)

        arr[x-1][y-1]=v
        ans=0
        l=0
        flag=0
        nik=0
        for i in range(n-1):
            if flag==1:
                break
            
            value=arr[0][i]
            for j in range(n):
                if flag==1:
                    break
                for k in range(m):
                    if k-j==nik:
                        print(value,arr[j][k],nik)
                        if value==arr[j][k]:
                            continue
                        else:
                            flag=1
                            break
            nik+=1
        if flag==1:
            print('No')
        else:
            print('Yes')