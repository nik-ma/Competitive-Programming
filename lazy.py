tc=int(input())
while tc:
    m,n,k,l=map(float,input().split(' '))
    p=n//(l+k)
    if (n-p*(l+k))/l>=1:
        h=((p+1)*1)//1
    else:
        h=(p*l+(n-(p*(k+l))))//1
    if h>m:
        print(int(m))
    else:
        print(int(h))

   
    
   
    tc-=1