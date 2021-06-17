import math
def countDivisors(n) : 
    cnt = 0
    for i in range(1, (int)(math.sqrt(n)) + 1) : 
        if (n % i == 0) : 
              
            # If divisors are equal, 
            # count only one 
            if (n / i == i) : 
                cnt = cnt + 1
            else : # Otherwise count both 
                cnt = cnt + 2
                  
    return cnt 
for _ in  range(int(input())):
    a,b=map(int,input().split())
    if a==b:
        print(-1)
    else:
        p=abs(b-a)
        print(countDivisors(b-a))

