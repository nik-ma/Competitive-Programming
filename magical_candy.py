from collections import Counter
import string
import math
import sys
# sys.setrecursionlimit(10**6) 
from fractions import Fraction
def debug(value):
    s=str(value)
    print(s)
    return
def array_int():
    return [int(i) for i in sys.stdin.readline().split()]
def vary(arrber_of_variables):
    if arrber_of_variables==1:
        return int(sys.stdin.readline())
    if arrber_of_variables>=2:
        return map(int,sys.stdin.readline().split()) 
def makedict(var):
    return dict(Counter(var))
mod=10**9+7
for _ in range(vary(1)):
    n=vary(1)
    num=array_int()
    if num.count(1)==0:
        evens=[0 for i in range(n)]
        evens[0]+=(num[0]-num[0]%2)
        for i in range(1,n-1):
            evens[i]=evens[i-1]+num[i]-num[i]%2
        evens[n-1]=evens[n-2]+(num[n-1] if num[n-1]%2!=0 else (num[n-1]-1))
        # print(evens)
        for _ in range(vary(1)): 
            r=vary(1)
            if n==1:
                if num[0]%2!=0:
                    ans=(num[0]*r)
                    ans=ans%mod
                else:
                    ans=((num[0]-1)*(r-1)+num[0])
                    ans=ans%mod
                continue
            if r%n==0:
                print(((evens[n-1]*(r//n))+(1 if num[n-1]%2==0 else 0))%mod)
            else:
                print(((evens[n-1]*(r//n))+evens[r%n-1]+(1 if num[r%n-1]%2!=0 else 0))%mod)
    else:
        if n==1:
            for _ in range(vary(1)):
                r=vary(1)
                if num[0]%2!=0:
                    ans=(num[0]*r)
                    print(ans%mod)
                else:
                    ans=((num[0]-1)*(r-1)+num[0])
                    print(ans%mod)

            
        else:
            if num.index(1)==0:
                for _ in range(vary(1)):
                    r=vary(1)
                    if r<=n:
                        print(1%)
                    else:
                        ans=1*(r//n)
                        if r%n==1 or r%n==0:
                            print(ans%mod)
                        else:
                            print((ans+1)%mod)

            else:
                if num.index(1)==n-1:
                    evens=[0 for i in range(n)]
                    evens[0]+=(num[0]-num[0]%2)
                    for i in range(1,n-1):
                        evens[i]=evens[i-1]+num[i]-num[i]%2
                    evens[n-1]=evens[n-2]+1
                    for _ in range(vary(1)):
                        r=vary(1)
                        # debug('first')
                        if r%n!=0:
                            ans1=((evens[n-1]*(r//n)+evens[r%n-1]+(1 if num[r%n-1]%2!=0 else 0))%mod)
                        else:
                            ans1=((evens[n-1]*(r//n))%mod)
                        print(ans1%mod)
                else:
                    evens=[0 for i in range(n)]
                    index=num.index(1)
                    evens[0]+=num[0]-num[0]%2
                    for i in range(1,n):
                        evens[i]+=evens[i-1]+num[i]-num[i]%2
                    ans=evens[n-1]
                    # print(evens)
                    for _ in range(vary(1)):
                        r=vary(1)
                        if r%n==0:
                            if num[index-1]%2!=0:
                                if num[n-1]%2!=0:
                                    ans1=((ans+2)*(r//n))
                                    # print(ans1%mod)
                                else:
                                    ans1=((ans)*(r//n)+1)
                                    # print(ans1%mod)
                            else:
                                if num[n-1]%2!=0:
                                    ans1=((ans)*(r//n))
                                    # print(ans1%mod)
                                else:
                                    ans1=((ans-2)*(r//n)+1)
                                    # print(ans1%mod)
                        else:
                            if r<n:
                                if r==index+1:
                                    ans1=evens[index]+1
                                    # print(ans1%mod)
                                else:
                                    if r<index+1:
                                        ans1=evens[r-1]+(1 if num[r-1]%2!=0 else 0)
                                        # print(ans1%mod)
                                    else:
                                        ans1=evens[r%n-1]+(-1 if num[index-1]%2==0 else 1)+(1 if num[r%n-1]%2!=0 else 0)

                                        # print(ans1%mod)
                            else:
                                if r%n!=0:
                                    if num[index-1]%2!=0:
                                        if num[n-1]%2!=0:
                                            ans1=((ans+2)*(r//n))
                                            if r%n==index+1:
                                                ans1+=evens[r%n-1]+1
                                                # print(ans1%mod)
                                            elif r%n<index+1:
                                                ans1+=evens[r%n-1]+(1 if num[r%n-1]%2!=0 else 0)
                                                # print(ans1%mod)
                                            else:
                                                ans1+=evens[r%n-1]+(-1 if num[index-1]%2==0 else 1)+(1 if num[r%n-1]%2!=0 else 0)

                                                # print(ans1%mod)
                                        else:
                                            ans1=((ans)*(r//n))
                                            if r%n==index+1:
                                                ans1+=evens[r%n-1]+1
                                                # print(ans1%mod)
                                            elif r%n<index+1:
                                                ans1+=evens[r%n-1]+(1 if num[r%n-1]%2!=0 else 0)
                                                # print(ans1%mod)
                                            else:
                                                ans1+=evens[r%n-1]+(-1 if num[index-1]%2==0 else 1)+(1 if num[r%n-1]%2!=0 else 0)

                                                # print(ans1%mod)
                                            
                                    else:
                                        if num[n-1]%2!=0:
                                            ans1=((ans)*(r//n))
                                            if r%n==index+1:
                                                ans1+=evens[r%n-1]+1
                                                # print(ans1%mod)
                                            elif r%n<index+1:
                                                ans1+=evens[r%n-1]+(1 if num[r%n-1]%2!=0 else 0)
                                                # print(ans1%mod)
                                            else:
                                                ans1+=evens[r%n-1]+(-1 if num[index-1]%2==0 else 1)+(1 if num[r%n-1]%2!=0 else 0)

                                                # print(ans1%mod)
                                        else:
                                            ans1=((ans-2)*(r//n))
                                            if r%n==index+1:
                                                ans1+=evens[r%n-1]+1
                                                # print(ans1%mod)
                                            elif r%n<index+1:
                                                ans1+=evens[r%n-1]+(1 if num[r%n-1]%2!=0 else 0)
                                                # print(ans1%mod)
                                            else:
                                                ans1+=evens[r%n-1]+(-1 if num[index-1]%2==0 else 1)+(1 if num[r%n-1]%2!=0 else 0)
                                                # print(ans1%mod)
                        print(ans1%mod)