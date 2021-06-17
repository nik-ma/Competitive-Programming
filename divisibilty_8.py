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
def isSubSequence(str1,str2): 
    m = len(str1) 
    n = len(str2) 
      
    j = 0    # Index of str1 
    i = 0    # Index of str2 
      
    # Traverse both str1 and str2 
    # Compare current character of str2 with  
    # first unmatched character of str1 
    # If matched, then move ahead in str1 
      
    while j<m and i<n: 
        if str1[j] == str2[i]:     
            j = j+1    
        i = i + 1
          
    # If all characters of str1 matched, then j is equal to m 
    return j==m 
n=input()
for i in range(0,1000,8):
    if isSubSequence(str(i),n):
        print('YES')
        print(i)
        break
else:
    print('NO')


            


