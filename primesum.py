'''import math
prime=[]
prime.append(2)
for num in range(3,2*100000,2):
    if all(num%i!=0 for i in range(3,int(math.sqrt(num))+1, 2)):
        prime.append(num)
#print(len(prime))
prime_pro=2*prime[0]+2*prime[1]+2*prime[2]'''
for _ in range(int(input())):
    n=int(input())
    if n>30:
        print('YES')
        if n-30!=6 and n-30!=14 and n-30!=10:
            print(2*3,2*5,2*7,n-30)
        else:
            print(2*3,2*5,2*7,n-31)

    else:
        print('NO')