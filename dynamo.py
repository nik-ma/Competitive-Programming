tc=int(input())
while tc:
    n=int(input())
    a=int(input())
    print(2*(10**n)+a,flush=True)
    b=int(input())
    print((10**n)-b,flush=True)
    c=int(input())
    print((10**n)-c,flush=True)
    tc-=1
    if int(input())==1:
        continue
    else:
        break


    
