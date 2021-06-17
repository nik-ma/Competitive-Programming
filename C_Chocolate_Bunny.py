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
testcases=1
for _ in range(testcases):
    n=vary(1)
    i=0
    j=n-1
    arr=[1 for i in range(n)]
    while i<j:
        print('?',i+1,j+1)
        sys.stdout.flush()
        k=vary(1)
        print('?',j+1,i+1)
        sys.stdout.flush()
        k2=vary(1)
        if k>k2:
            arr[i]=k
            i+=1
        else:
            arr[j]=k2
            j-=1
    st=set()
    for t in range(1,n+1):
        st.add(t)
    for t in range(len(arr)):
        if t!=i:
            st.remove(arr[t])
    for t in st:
        arr[i]=t
    print('!',*arr)
    
        


