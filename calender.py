from collections import Counter
import string
import math
dicti={'1':31,'2':28,'3':31,'4':30,'5':31,'6':30,'7':31,'8':31
    ,'9':30,'10':31,'11':30,'12':31}
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

from datetime import date
print(abs((date(*map(int,input().split(':')))-date(*map(int,input().split(':')))).days))
        





