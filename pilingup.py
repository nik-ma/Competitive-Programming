# Enter your code here. Read input from STDIN. Print output to STDOUT
tc=int(input())
while tc:
    n=int(input())
    l=list(map(int,input().split(' ')))
    if l[0]>=l[n-1]:
        c=l.pop(0)
    else:
        c=l.pop(n-1)

    for i in range(len(l)): 
        if c<l[0] or c<l[len(l)-1]:
            print("No")
            break
        else:
            if l[0]>=l[len(l)-1]:
                c=l.pop(0)
            else:
                c=l.pop(len(l)-1)
    else:
        print('Yes')        
    tc-=1


          

