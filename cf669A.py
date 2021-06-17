from collections import Counter
import string
import math
def binomialCoeff(n , k):
    if n<k:
        return 1 
    C = [0 for i in range(k+1)] 
    C[0] = 1
    for i in range(1,n+1): 
        j = min(i ,k) 
        while (j>0): 
            C[j] = C[j] + C[j-1] 
            j -= 1
    return C[k] 
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
for _ in range(int(input())):
    n=vary(1)
    num=array_int()
    t=makedict(num)
    one,zero=0,0
    for i in t:
        if i==1:
            one+=t[i]
        else:
            zero+=t[i]
    if one<=zero:
        print(n//2)
        print(*[0 for i in range(n//2)])
    elif one>zero:
        if (n//2)%2!=0:
            print(n//2+1)
            print(*[1 for i in range(n//2+1)])
        else:
            print(n//2)
            print(*[1 for i in range(n//2)])
    

    

        
            

        
        


