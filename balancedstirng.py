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
    n,k=vary(2)
    s=input()
    onesi=0
    quesi=0
    zerosi=0
    ones=0
    ques=0
    zeros=0
    st=s[0:k]
    try:
        onesi=st.count('1')
    except:
        pass
    try:
        zerosi=st.count('0')
    except:
        pass
    try:
        quesi=st.count('?')
    except:
        pass
    print(onesi,zerosi,quesi)
    for i in range(1,n-k+1):
        st=s[i:i+k]
        try:
            ones=st.count('1')
        except:
            pass
        try:
            zeros=st.count('0')
        except:
            pass
        try:
            ques=st.count('?')
        except:
            pass
        print(ones,zeros,ques)
        if (ones==onesi and zerosi==zeros and quesi==ques) or ques==k//2:
            continue
        else:
            print('NO')
            break
    else:
        print('YES')

        




