from collections import Counter
def argument(i,j,count):
    return j-i+1-count
for _ in range(int(input())):
    n,k=map(int,input().split())
    f=[int(x) for x in input().split()]
    repeated=0
    position=[[-1 for i in range(n)] for i in range(n)]
    for i in range(n):
        dictu={}
        count=0
        for j in range(i,n):
            if f[j] in dictu and dictu[f[j]]==1:
                dictu[f[j]]+=1
                count-=1
            elif f[j] not in dictu:
                dictu[f[j]]=1
                count+=1
            position[i][j]=argument(i,j,count)
    listut=[[0,n-1]]
    answer=0
    while 1:
        if len(listut)==0:
            break
        elements=listut.pop()
        intial_arg=position[elements[0]][elements[1]]
        after=2**32
        pointer=-1
        for i in range(elements[0],elements[1]):
            #print(elements[i],elements[1])
            temporary=position[elements[0]][elements[1]]+position[i+1][elements[1]]
            if after>=temporary:
                after=temporary
                pointer=i
        if intial_arg>=after+k:
            listut.append([pointer+1,elements[1]])
            listut.append([0,pointer])
        else:
            answer+=intial_arg+k
    print(answer)




                

        

    
   
             
         

        
        
            
        

