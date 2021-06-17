# cook your dish here
from collections import Counter
import string
import math
import sys
import random
# sys.setrecursionlimit(10**6) 
from fractions import Fraction
def array_int():
    return [int(i) for i in sys.stdin.readline().split()]
def vary(arrber_of_variables):
    if arrber_of_variables==1:
        return int(sys.stdin.readline())
    if arrber_of_variables>=2:
        return map(int,sys.stdin.readline().split()) 
def solve(n,e,h,a,b,c):
    if n<=0:
        return 0
    mini=2**32
    if e//2>=n:
        mini=min(mini,n*a)
    if h//3>=n:
        mini=min(mini,n*b)
    if n<=e and n<=h:
        mini=min(mini,n*c)
    if e//2>=1 and (e//2>=(3*n-h+2)//3):
        if a-b<0:
            rem=min(n-1,e//2)
            mini=min(mini,(a-b)*rem+n*b)
        else:
            rem=max(1,(3*n-h+2)/3)
            mini=min(mini,(a-b)*rem+n*b)
    if e-n>=1 and e-n>=n-h:
        if a-c<0:
            rem=min(n-1,e-n)
            ans=min(mini,(a-c)*rem+n*c)
        else:
            rem=min(1,n-h)
            mini=min(mini,(a-c)*rem+n*c)		
    if e>=3 and h>=4 and n>=3:
        mini=min(mini,a+b+c+solve(n-3,e-3,h-4,a,b,c))
    return mini
	

def makedict(var):
    return dict(Counter(var))
testcases=vary(1)
for tt in range(testcases):
    n,e,h,a,b,c=vary(5)
    # print(n,e,h,a,b,c)
    
    # print('case',tt+1)
    # n=random.randint(1,100)
    # e=random.randint(1,100)
    # h=random.randint(1,100)
    # a=random.randint(1,100)
    # b=random.randint(1,100)
    # c=random.randint(1,100)
    if e==h and e<n:
        print(-1)
    elif e<h and e+(h-e)//3<n:
        print(-1)
    elif h<e and h+(e-h)//2<n:
        print(-1)
    else:
        listi=[a,b,c]
        listi.sort()
        ans=0
        if c==listi[0]:
            if min(e,h)>=n:
                ans+=c*n
            else:
                rem=n-min(e,h)
                z=min(e,h)
                h-=z
                e-=z
                ans+=(z)*c
                if b==listi[1]:
                    value=h//3
                    if value>=rem:
                        ans+=(rem)*b
                    else:
                        ans+=value*b
                        ans+=(rem-value)*a
                else:
                    value=e//2
                    if value>=rem:
                        ans+=(rem)*a
                    else:
                        ans+=value*a
                        ans+=(rem-value)*b
            print(ans)
        else:
            mini=2**32
            mini=solve(n,e,h,a,b,c)
            if mini<2**32:
                print(mini)
            else:
                print(-1)
                