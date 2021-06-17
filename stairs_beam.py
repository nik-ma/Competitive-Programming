for _ in range(int(input())):
    n=int(input())
    maxin=-1
    num=[int(i) for i in input().split()]
    ans=0
    k=0
    i=0
    while i<n-1:
        if num[i]<=num[i+1]:
            i+=1
            continue
        else:
            for j in range(i,n):
                if num[i]>num[j]:
                    k=num[i]-num[j]
                    if k>maxin:
                        maxin=k
                    else:
                        
                        continue
                else:
                    i=j
                    break
            else:
                i=n-1
        ans+=maxin
    print(ans)     
            
