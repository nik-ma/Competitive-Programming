from collections import Counter
import string
import math
import sys
#sys.setrecursionlimit(10**6) 
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
for _ in range(vary(1)):
    n,k=vary(2)
    s=input()
    iron_i=0
    magnet_i=0
    sheets=0
    
    count=0
    
    while iron_i<len(s) and magnet_i<len(s):
        if s[iron_i]=='M':
            if s[magnet_i]=='I':
                power=k+1-abs(iron_i-magnet_i)-sheets
                if power>0:
                    count+=1
                    iron_i+=1
                    magnet_i+=1
                else:
                    if iron_i>magnet_i:
                        magnet_i+=1
                    else:
                        iron_i+=1
            elif s[magnet_i]=='X':
                sheets=0
                iron_i=magnet_i
                iron_i+=1
                magnet_i+=1
            elif s[magnet_i]==':':
                magnet_i+=1
                sheets+=1
            else:
                magnet_i+=1
        elif s[iron_i]=='X':
            magnet_i=iron_i
            sheets=0
            magnet_i+=1
            iron_i+=1
        elif s[iron_i]==':':
            sheets+=1
            iron_i+=1
        else:
            iron_i+=1
    print(count)
            
            



         
