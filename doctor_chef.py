for _ in range(int(input())):
    n,vaccine=map(int,input().split())
    infected=[int(x) for x in input().split()]
    infected.sort()
    days=0
    count=0
    ind=-1
    if infected[-1]<=vaccine:
        print(n)
        continue
    for i in range(n):
        if vaccine>=infected[i]:
            count+=1
            ind=i
        else:
            break
    #print(ind)
    #print(count)
    if 2*infected[ind] >vaccine and ind!=-1:
        vaccine=2*infected[i-1]
    #print(vaccine)
    for i in range(count,n):
       #print(infected[i],vaccine)
        while(infected[i]>vaccine):
            #print('hello')
            vaccine*=2
            days+=1
        days+=1
        vaccine=(infected[i])*2
    #print(days)
    print(days+count) 