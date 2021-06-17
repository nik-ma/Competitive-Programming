for _ in range(int(input())):
    listm=[]
    n=int(input())
    list1=list(map(int,input().split()))[:n]
    for i in range(0,n):
        c=0
        afternnoi=[]
        afterin=[]
        prevnoi=[]
        previn=[]
        for j in range (0,n):
            if i==j:
                continue
            elif i<j:
                
                if list1[j]>=list1[i]:
                    afternnoi.append(list1[j])
                if list1[j]<list1[i]:
                    afterin.append(list1[j])
                    c=c+1
            else:
                if list1[j]<=list1[i]:
                    prevnoi.append(list1[j])
                if list1[j]>list1[i]:
                    previn.append(list1[j])
                    c=c+1
        try:        
            p=max(previn)
            for k in afternnoi:
                if p>k:
                    c=c+1
        except :
            pass
        try:        
            q=min(afterin)  
            for l in prevnoi:
                if q<l:
                   c=c+1
        except:
            pass
        listm.append(c)      
        print(c)
        print(afterin,afternnoi,previn,prevnoi) 
    print(min(listm)+1,max(listm)+1)