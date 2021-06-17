# cook your dish here
import math
for i in range(int(input())):
    n,p=map(int,input().split())
    d=[int(x) for x in (input().split())]
    d1=d
    ni=[]
    M=0
    ac=0
    ad=0
    for i in range(n):
        if p%d[i]==0:
            M+=1
            ni.append((p//d[i])-1)
            
        else:
            if p<d[i]:
                ab=[0]*n
                ab[i]=1
                print("YES",ab)
                ac=1
                break
            else:
                ac=[0]*n
                ac[i]=math.ceil(p/d[i])
                ad=1
                print("YES",ac)
                break
    if ac==1 or ad==1:
        continue
    if M==n:
        d1.sort()
        
        for i in range(n-1):
            k=d.index(d1[len(d1)-1-i])
            st=p-ni[k]*d[k]
            if st<d[k-1]:
                ni
                print("YES",)



                 


       
       
        
        






        
            
        

   
