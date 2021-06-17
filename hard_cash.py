for i in range(int(input())):
    n,k=map(int,input().split())
    a=[int(i) for i in input().split()]
    l=[]
    s=0
    for i in range(n):
        l.append((k-a[i]%k)%k)
        s+=l[i]
    p=l[0]
    r=a[0]
    if n>1:
        for i in range(1,n):
            if r>s-p:
                rem=(r-s+p)
                break
            if r==s-p:
                rem=0
                break
            if r<s-p:
                r+=a[i]
                p+=l[i]
        else:
            rem=s
    else:
        rem=r%k
    print(rem%k)


    
        



