from collections import Counter
import string
import math
import sys
#sys.setrecursionlimit(10**6)
def array_int():
    return [int(i) for i in sys.stdin.readline().split()]
def vary(number_of_variables):
    if number_of_variables==1:
        return int(sys.stdin.readline())
    if number_of_variables>=2:
        return map(int,sys.stdin.readline().split()) 
def makedict(var):
    return dict(Counter(var))
def countBits(number):
    return int((math.log(number)/math.log(2)) + 1)
# print(bin(5).count('1'))
for _ in range(vary(1)):
    n=vary(1)
    if n==1:
        print(1)
        continue
    if bin(n).count('1')==1:
        print(-1)
        continue
    arr=[2,3,1,5,4]
    if n<=5:
        print(*arr[:n])
        continue
    i=6
    while i<=n:
        if bin(i).count('1')==1:
            arr.extend((i+1,i))
            i+=2
        else:
            arr.append(i)
            i+=1
    print(*arr)
    
