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
mod=998244353
fact=[1]*100001
c=1
for i in range(1,100001):
    fact[i]=(c*i)%mod
    c=fact[i]
for _ in range(int(input())):
    s=input()
    st=makedict(list(s))
    q=vary(1)
    for i in range(q):
        sub=input()
        subt=makedict(list(sub))
        count=1
        countapp=[]
        countapp2=[]
        for j in subt:
            if j in st:
        
                if st[j]>=subt[j]:
                    count=(count*fact[st[j]]//(fact[st[j]-subt[j]]*fact[subt[j]]))%mod
                else:
                    count=0
                    break
            else:
                count=0
                break
        countapp.append(count)
        countapp2.append(sub)
        print(count)
    ff=max(count)
    if ff:
        for i in range(q):
            if ff==countapp[i]:
                print(countapp2[i])
                break
    else:
        print('No Research This Month')

        
                    
            


    
    
    
