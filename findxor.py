from collections import Counter
import string
import math
import sys
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
# print(2**19)
def countBits(number):
    return int((math.log(number)/math.log(2)) + 1)
#print(countBits(1000000))
for _ in range(int(input())):
    n=vary(1)
    ans=''
    print(1,2**20)
    sys.stdout.flush()
    orig_sum=(vary(1))-n*(2**20)
    #tt=countBits(orig_sum)
    for i in range(19,0,-1):
        print(1,2**i)
        sys.stdout.flush()
        fake_sum=vary(1)
        if fake_sum-n*(2**i)==orig_sum:
            ans+='0'
            continue
        if fake_sum==orig_sum:
            if (n//2)%2!=0:
                ans+='1'
            else:
                ans+='0'
            continue
        if fake_sum<orig_sum:
            ones=(n+((orig_sum-fake_sum)//(2**i)))//2
            if ones%2!=0:
                ans+='1'
            else:
                ans+='0'
            continue
        if fake_sum>orig_sum:
            ones=(n-((fake_sum-orig_sum)//(2**i)))//2
            if ones%2!=0:
                ans+='1'
            else:
                ans+='0'
            continue
    if orig_sum%2!=0:
        ans+='1'
    else:
        ans+='0'
    print(2,int(ans,2))
    sys.stdout.flush()
    if vary(1)==1:
        continue
    else:
        quit()