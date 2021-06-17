from collections import Counter
import string
import math
def array_int():
    return [int(i) for i in input().split()]
def vary(number_of_variables):
    if number_of_variables==1:
        return int(input())
    if number_of_variables>=2:
        return map(int,input().split()) 
def makedict(var):
    return dict(Counter(var))
mod=1000000007
if 1:
    n,m=vary(2)
    if 1:
        if n==1:
            print(1)
        elif n==2:
            if m!=2:
                print(2)
            else:
                print(1)
        else:
            if n%2!=0:
                if n//2+1<=m:
                    print(m-1)
                else:
                    print(m+1)
            else:
                if n//2>=m:
                    print(m+1)
                else:
                    print(m-1)
            





