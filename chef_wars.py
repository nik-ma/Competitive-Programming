for _ in range(int(input())):
    h,p=map(int,input().split())
    flag=0
    if p>=h:
        print(1)
        continue
    while h>0:
        if p==0:
            print(0)
            flag=-1
            break
        h-=p
        #print(h)
        p=p//2
        #print(p)
    #print(h,p)
    if flag!=-1:
        print(1)
        