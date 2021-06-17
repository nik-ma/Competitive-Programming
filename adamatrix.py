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
global mat

def transpose(N): 
    global mat,matb
    for i in range(N): 
        for j in range(i):
            mat[i][j],mat[j][i]=mat[j][i],mat[i][j]

    #print(mat)
for _ in range(vary(1)):
    n=vary(1)
    matb=[[0 for i in range(n)] for j in range(n)]
    mat=[]
    for i in range(n):
        mat.append(array_int())
    count=0
    for i in range(n-1,-1,-1):
        if mat[0][i]!=i+1:
            transpose(i+1)
            #print(mat)
            count+=1
    print(count)




