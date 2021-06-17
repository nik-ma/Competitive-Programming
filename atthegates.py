for i in range(int(input())):
    n,k=map(int,input().split())
    a=[i for i in input().split()]
    len_a=len(a)
    for i in range(len_a-1,len_a-k-1,-1):
        if a[i]=='H':
            a.pop(i)
            p=len(a)
            for j in range(p):
                if a[j]=='H':
                    a[j]='T'
                else:
                    a[j]='H'
        else:
            a.pop(i)
         
    print(a.count('H'))

        


