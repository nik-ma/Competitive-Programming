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
m,n=vary(2)
mat=[]
for i in range(m):
    mat.append(array_int())
pat=[]
for i in range(m):
    pat.append([int(-2) for j in range(n)])
for i in range(m):
    for j in range(n):
        if mat[i][j]==0:
            for k in range(n):
                pat[i][k]=0
            for k in range(m):
                pat[k][j]=0
for i in range(m):
    for j in range(n):
        if pat[i][j]==-2:
            pat[i][j]=1

""" for i in range(m):
    print(*pat[i]) """
cat=[]
for i in range(m):
    cat.append([0 for j in range(n)])
for i in range(m):
    for j in range(n):
        for k in range(n):
            if pat[i][k]==1:
                cat[i][j]=1
                
        for k in range(m):
            if pat[k][j]==1:
                cat[i][j]=1
""" print(cat)
print(mat)
print(pat) """
if cat==mat:
    print('YES')
    for i in range(m):
        print(*pat[i])
else:
    print('NO')

                
        
        


