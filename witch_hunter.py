from collections import Counter
import string
import math
def binomialCoeff(n , k): 
    C = [0 for i in range(k+1)] 
    C[0] = 1
    for i in range(1,n+1): 
        j = min(i ,k) 
        while (j>0): 
            C[j] = C[j] + C[j-1] 
            j -= 1
    return C[k] 
import datetime as dt
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
from datetime import datetime
def LCMofArray(a):
  lcm = a[0]
  for i in range(1,len(a)):
    lcm = lcm*a[i]//math.gcd(lcm, a[i])
  return lcm
def convert(n): 
    return str(dt.timedelta(seconds = n)) 
for _ in range(vary(1)):
    n=vary(1)
    num=array_int()
    value=LCMofArray(num)
    value=(convert(value))
    s2='09:30:00'
    s1=str(value)
    FMT = '%H:%M:%S'
    tdelta = datetime.strptime(s2, FMT) - datetime.strptime(s1, FMT)
    print(tdelta)

        
        
