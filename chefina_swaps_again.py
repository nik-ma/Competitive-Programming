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
for _ in range(int(input())):
    n=vary(1)
    titu=(n*(n+1))//2
    if titu%2!=0:
        print(0)
        continue
    """ num=[i for i in range(1,n+1)]
    num2=num[:] """
    swaps=0
    titu=titu//2
    sumt=0
    x=(-1+(pow(1+(titu*2)*4,0.5)))/2
    #print(x)
    tt=int(x)
    if math.ceil(x)==x:
        swaps+=((tt*(tt-1))//2)+((n-tt)*(n-tt-1))//2
    tt=int(x)

    swaps+=n-tt
    """ for i in range(n-1,-1,-1):
        if sumt<titu:
            sumt+=num[i]
            swaps+=1
            tt=i
            continue
        else:
            break """
    
    print(swaps)
       


            


    
                


            


    


