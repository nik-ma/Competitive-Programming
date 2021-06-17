for _ in range(int(input())):
    n=int(input())
    l=[int(x) for x in input().split()]
    diff=[]
    p=[]
    if n==2:
        z=abs(l[0]-l[1])
        if z>2:
            print(1,1)
        else:
            print(2,2)
    else:
        
            diff = [l[i + 1] - l[i] for i in range(len(l)-1)] 
            minu,maxu=1,1
            counter=1
            for i in range(len(diff)):
                if diff[i]<=2:
                    counter+=1
                    if i==len(diff)-1 and maxu<counter:
                        maxu=counter
                        counter=1
                elif maxu<counter:
                    maxu=counter
                    counter=1
            
                    