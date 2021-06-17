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
def SieveOfEratosthenes(n): 
    global primes
    # Create a boolean array "prime[0..n]" and initialize 
    #  all entries it as true. A value in prime[i] will 
    # finally be false if i is Not a prime, else true. 
    prime = [True for i in range(n+1)] 
    p = 2
    while (p * p <= n): 
          
        # If prime[p] is not changed, then it is a prime 
        if (prime[p] == True): 
              
            # Update all multiples of p 
            for i in range(p * p, n+1, p): 
                prime[i] = False
        p += 1
      
    # Print all prime numbers 
    for p in range(2, n+1): 
        if prime[p]: 
            primes.append(p)
primes=[]
SieveOfEratosthenes(2*(10**6))
for _ in range(vary(1)):
    n=vary(1)
    b=array_int()
    # print(len(primes))
    pt=set(b)
    dic={}
    j=0
    for i in pt:
        dic[i]=primes[j]
        j+=1
    for i in range(n):
        print(dic[b[i]],end=" ")
    print()


    
    
    
        
        