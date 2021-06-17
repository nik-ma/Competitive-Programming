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
n,k=vary(2)
mat=[[0 for i in range(n)] for i in range(n)]
for i in range(k):
    x,y,l,r=vary(4)
    mat[x-1][y-1]=i+1
# for i in range(n):
#     for j in range(n):
#         print(mat[i][j],end=" ")
#     print()

