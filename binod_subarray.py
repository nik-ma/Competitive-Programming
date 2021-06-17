# cook your dish here
import sys
n,k,s=map(int,sys.stdin.readline().split())
num=[int(i) for i in sys.stdin.readline().split()]

if n<=10000 and k<=10000:
    l=[]
    flag=0
    maxi=2**32
    kt=-1
    sum2=sum(num[0:k+1])
    for i in range(n):
        if i!=0 and i+k<n:
            kt=0
            sum2=sum3-num[i-1]+num[i+k]
        if i!=0 and kt!=0:
            break
        
        if sum2>s:
            l.append(k+1)
            flag=-1
            break
        sum3=sum2
        for j in range(i+k+1,n):
            if maxi<(j-i+1):
                
                break
            
            if sum2+num[j]>s:
                flag=-1
                l.append(j-i+1)
                maxi=j-i+1
                break
            sum2+=num[j]
    #print(l)
    if flag==0:
        print(-1)
    else:
        print(min(l))
else:
    l=[]
    flag=0
    maxi=-1
    kt=-1
    sum2=sum(num[0:k+1])
    for i in range(n):
        if i!=0 and i+k<n:
            kt=0
            sum2=sum3-num[i-1]+num[i+k]
        if i!=0 and kt!=0:
            break
        
        if sum2>s:
            l.append(k+1)
            flag=-1
            break
        sum3=sum2
        for j in range(i+k+1,n):
            if maxi>(j-i+1):
                
                break
            
            if sum2+num[j]>s:
                flag=-1
                l.append(j-i+1)
                maxi=j-i+1
                break
            sum2+=num[j]
    #print(l)
    if flag==0:
        print(-1)
    else:
        print(min(l))






        