for _ in range(int(input())):
    n=int(input())
    a=[int(i) for i in input().split()]
    b=[int(i) for i in input().split()]
    l=set(a+b)
    
    print(l)
    l=list(l)
    l.sort()
    summ_a=[]
    summ_b=[]
    dic_a={}
    dic_b={}
    dic_sum={}
    score=0
    for i in a:
        if str(i) in dic_a:
            dic_a[str(i)]+=1
        else:
            dic_a[str(i)]=1
    print(dic_a)
    for i in b:
        if str(i) in dic_b:
            dic_b[str(i)]+=1
        else:
            dic_b[str(i)]=1
    print(dic_b)
    for i in l:
        count=0
        if str(i) in dic_a:
            count+=dic_a[str(i)]
        if str(i) in dic_b:
            count+=dic_b[str(i)]
        
        if count%2!=0:
            
            print(-1)
            break
        else:
            if str(i) in dic_a:
                sub1=dic_a[str(i)]
            else:
                sub1=0
            if str(i) in dic_b:
                sub2=dic_b[str(i)]
            else:
                sub2=0
            if sub1-sub2>0:
                for ni in range((abs(sub2-sub1)//2)):
                    summ_a.append(i)
                
            elif sub1-sub2<0:
                for ni in range((abs(sub2-sub1)//2)):
                    summ_b.append(i)
                
            else:
                continue
    else:
        if len(summ_a)==0:
            print(0)
            continue
        print(summ_a)
        summ_a.sort()
        
        summ_b.sort(reverse=True)
        print(summ_b)
        mini=min(l)
        for i in range(len(summ_a)):
            if min(summ_a[i],summ_b[i])<=mini*2:
                score+=min(summ_a[i],summ_b[i])
            else:
                score+=mini*2
        print(score)
        '''print(summ_a)
        print(summ_b)
        cou=sum(summ_a)
        j=0
        i=0
        while i<cou:
            if summ_a[j]!=0:
                if i+summ_a[j]>cou:
                    score+=l[j]*((i+summ_a[j])-cou)
                    
                    i+=summ_a[j]
                    break
                else:
                    score+=l[j]*(summ_a[j])
                    i+=summ_a[j]
                
            else:
                if i+summ_b[j]>cou:
                    score+=l[j]*((i+summ_b[j])-cou)
                    
                    i+=summ_b[j]
                    break
                else:
                    score+=l[j]*(summ_b[j])
                    i+=summ_b[j]

            j+=1'''
        
        