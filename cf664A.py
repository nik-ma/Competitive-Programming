for _ in range(int(input())):
    
    f=[int(x) for x in input().split()]
    count=0
    for i in f:
        if i%2!=0:
            count+=1
    if min(f)==0:
        if count%2==0:
            print("YES")
            continue
        elif count==1:
            print("YES")
            continue
        else:
            print("NO")
            continue
    
    if count%2==0:
        print("NO")
    else:
        print("YES")
    
    '''if count==0:
        print("YES")
        continue
    if count==4:
        print("YES")
        continue
    if count==3:
        print("YES")
        continue
    if count==2:
        print("NO")
    if count==1:
        print("YES")'''

