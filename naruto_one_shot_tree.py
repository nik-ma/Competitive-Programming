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
def print2largest(arr, arr_size): 
  
    # There should be atleast 
        # two elements  
    if (arr_size < 2): 
        return -1
      
  
    first = second = -2147483648
    for i in range(arr_size): 
 
        if (arr[i] >=first): 
          
            second = first 
            first = arr[i] 
        elif (arr[i] >=second and arr[i] != first): 
            second = arr[i] 
      
    if (second == -2147483648): 
        return -1
    else: 
        return second

for _ in range(int(input())):
    n=vary(1)
    
    graph=[[0 for i in range(n+1)] for i in range(n+1)]
    visited=[[0 for i in range(n+1)] for i in range(n+1)]
    count=[0]*(n+1)
    for i in range(n-1):
        u,v=vary(2)
        graph[u].append(v)
        count[u]+=1

        graph[v].append(u)
        count[v]+=1
    maxi=0
    for i in range(1,n+1):
        if maxi>count[i]:
            maxi=count[i]
    print(maxi)






    
