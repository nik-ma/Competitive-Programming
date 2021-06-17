def modInverse(a, m) : 
      
    g = gcd(a, m) 
      
    if (g != 1) : 
        print("Inverse doesn't exist") 
          
    else :
          
        # If a and m are relatively prime, 
        # then modulo inverse is a^(m-2) mode m 
        return power2(a, m - 2, m)
         
      
# To compute x^y under modulo m 
def power2(x, y, m) : 
      
    if (y == 0) : 
        return 1
          
    p = power2(x, y // 2, m) % m 
    p = (p * p) % m 
  
    if(y % 2 == 0) : 
        return p  
    else :  
        return ((x * p) % m) 
  
# Function to return gcd of a and b 
def gcd(a, b) : 
    if (a == 0) : 
        return b 
          
    return gcd(b % a, a) 

import math
import string
for _ in range(int(input())):
    s=input()
    weight=list(map(int,input().split()))
    dict_w={}
    j=0
    l=[]
    dict_v={}
    for i in string.ascii_lowercase[:26]:
        dict_w[i]=weight[j]
        j+=1
    for i in range(len(s)):
        for j in range(i+1,len(s)+1):
            l.append(s[i:j])
    print(l)
    count=0
    for li in l:
        #print(type(li),li)
        if li in dict_v:
            dict_v[li]+=1
            count+=1
        else:
            count+=1
            dict_v[li]=1
    #print(dict_v)
    #print('hello')
    po=0
    #print('true')
    dict_i={}
    mnk=0
    #print('gaa')
    str_length=len(s)
    for i in l:
        length_i=len(i)
        print(length_i,str_length)
        if length_i<=str_length:
            dict_i[i]=dict_w[i[-1]]+po
            
            po=dict_i[i]
            if i+s[mnk:str_length]==i:
                power

            
        if length_i==str_length:
            po=0
            str_length-=1
    #print(dict_i)


    total_w=0
    #print(dict_v)
    for i in dict_v:
        z=len(i)
        power=0
        #print(i)
        #print(z)
        for j in range(1,z+1):
            #print(i[0:j])
            if (i[0:j]+i)[0:z]==i:
                power+=dict_i[i[0:j]]    
                #print(power)
        #print(i,power)
        total_w+=power*dict_v[i]
    print((modInverse(count,998244353)*total_w)%998244353)
    #print(dict_i)
    


    