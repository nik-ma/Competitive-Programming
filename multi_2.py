for _ in range(int(input())):
    n=int(input())
    count=0
    p=0
    dict={'1':0,'6':1,'36':2,'216':3,'1296':4,'7776':5,'46656':6,'279936':7,'1679616':8,'10077696':9,'362797056':10}
    if n==1:
        print(0)
        continue
    if n<6 and n==3:
        print(2)
        continue
    elif n<6:
        print(-1)
        continue
    while n>=6:
        if n%6!=0 and n%3!=0:
            print(-1)
            p=1
            break
        if n%6==0 and str(n) not in dict:
            if str(n*2) in dict:
                count+=1
                count+=dict[str(n*2)]
                p=1
                print(count)
                break
            else:
                count+=1
                n=n//6
        elif n%6==0 and str(n) in  dict:
            count+=dict[str(n)]
            p=1
            print(count)
            break
        elif n%6!=0 and n%3==0:
            if str(n*2) in dict:
                count+=1
                count+=dict[str(n*2)]
                p=1
                print(count)
                break
            else:
                n=n*2
                count+=1
    if p==0:
        print(-1)
        

        







    
