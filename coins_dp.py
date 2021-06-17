from collections import Counter
import string
import math
import sys
sys.setrecursionlimit(10**6)
def array_int():
    return [int(i) for i in sys.stdin.readline().split()]
def vary(number_of_variables):
    if number_of_variables==1:
        return int(sys.stdin.readline())
    if number_of_variables>=2:
        return map(int,sys.stdin.readline().split()) 
def makedict(var):
    return dict(Counter(var))
mod=100000007
count=0
string=""
def solve(i):
	global count,string
	n=len(string)
	if i>n:
		count+=1
		return
	solve(i+1)
	if i<n-1 and int(string[i:i+2])<27:
		solve(i+2)
string=input()
solve(0)
print(count)





 


    


    



