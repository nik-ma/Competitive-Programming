import math

_1_50 = 1 << 50  # 2**50 == 1,125,899,906,842,624

def isqrt(x):
    """Return the integer part of the square root of x, even for very
    large integer values."""
    if x < 0:
        raise ValueError('square root not defined for negative numbers')
    if x < _1_50:
        return int(math.sqrt(x))  # use math's sqrt() for small parameters
    n = int(x)
    if n <= 1:
        return n  # handle sqrt(0)==0, sqrt(1)==1
    # Make a high initial estimate of the result (a little lower is slower!!!)
    r = 1 << ((n.bit_length() + 1) >> 1)
    while True:
        newr = (r + n // r) >> 1  # next estimate by Newton-Raphson
        if newr >= r:
            return r
        r = newr
n,t=map(int,input().split())
for _ in range(n):
    num=int(input())
    if num<0:
        print('no')
        continue
    sqrt=isqrt(num)
    #print(sqrt)
    sqrt=sqrt**2
    p=(num*t)/100
    diff=num-sqrt
    #print(sqrt,p)

    if diff<=p:
        print('yes')
    else:
        print('no')

