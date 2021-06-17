import math
for _ in range(int(input())):
    n=int(input())
    l=list(map(int,input().split()))
    i=0
    j=1
    ans=-1
    max1=float("-inf")
    while(i<n-1):
        if j<n:
            val=(l[j]-l[i])/(j-i)
            if val>=max1:
                ans=max(ans,j-i)
                max1=val
                ind=j
            j+=1
        else:
            max1=float('-inf')
            i=ind
            j=ind+1
    print(ans)