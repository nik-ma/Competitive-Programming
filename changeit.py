tc=int(input())

while tc:
    n=int(input())
    lis=[]
    arry=input().split()
    count={}
    great= 0
    for i in arry:
        
        if i in count:
            count[i]+=1
        else:
            count[i]=1
        if count[i]>great:
            great=count[i]
    print(len(arry)-great)

    tc-=1
        

