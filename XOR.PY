def computeXOR(n) : 
  
    # Modulus operator are expensive  
    # on most of the computers. n & 3  
    # will be equivalent to n % 4. 
  
    # if n is multiple of 4  
    if n % 4 == 0 : 
        return n 
  
    # If n % 4 gives remainder 1 
    if n % 4 == 1 : 
        return 1
  
    # If n%4 gives remainder 2  
    if n % 4 == 2 : 
        return n + 1
  
    # If n%4 gives remainder 3 
    return 0

for _ in range(int(input())):
    l,r=map(int,input().split())
    print(computeXOR(l-1)^computeXOR(r))