import math,bisect
pro=1
'''def pri(n):
    global pro
    prime=[]
    prime.append(2)
    pro*=2
    for num in range(3,n+1,2):
        if all(num%i!=0 for i in range(3,int(math.sqrt(num))+1, 2)):
            prime.append(num)
            pro*=num
    return len(prime)'''
MAX = 100000
time=0
# array to store all prime less  
# than and equal to 10^6  
primes = []  
# utility function for  
# sieve of Eratosthenes  
def sieve():  
       
    isComposite = [False]*(MAX+1) 
    i = 2 
    while (i * i <= MAX):  
        if (isComposite[i] == False): 
            j = 2 
            while (j * i <= MAX): 
                isComposite[i * j] = True 
                j+=1 
        i+=1 
  
    # Store all prime numbers in  
    # vector primes[]  
    for i in range(2,MAX+1):  
        if (isComposite[i] == False):  
            primes.append(i) 
  
# Function to find LCM of  
# first n Natural Numbers 

# Driver code  
sieve()  

#print(prime)
for _ in range(int(input())):
    #global pro
    n=int(input())
    if n==1:
        print(0)
        continue
    if n==2:
        print(1)
        continue
    print(bisect.bisect(primes,n)+n-3)
    
    
    '''for i in range(n-1,1,-1):
        if pro==lc:
            break
        else:
            pro*=i
            time+=1'''
        
    print(time+n-2)
    #print(pro,lc)

    #print(primes)

    '''if pro!=lc:
        print(pri(n)+n-1)
    else:
        print(n-1)
    pro=1'''
    #print(lc,len(primes))    
