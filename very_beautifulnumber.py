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
p,x=vary(2)
ans=0
def find(b):
    global ans
    tt=((b*(pow(10,p-1,((10*x)-1))-x)))/((10*x)-1)
    #print(int(tt))
    if math.ceil(tt)==int(tt):
        if len(str(int(tt)))==p-1:
            ans=int(tt)
            return 1
        else:
            return 0
    else:
        return 0
for i in range(1,10):
    if find(i):
        print(ans*10+i)
        break
else:
    print('Impossible')



