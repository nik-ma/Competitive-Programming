def lexicographi_sort(s):
    return sorted(sorted(s), key=str.upper)
for _ in range(int(input())):
    s=input()
    p=input()
    s=list(s)
    #s_sorted=(lexicographi_sort(s))
    z=p[0:1]
    lenp=len(p)
    flag=0
    #print(s_sorted)
    for i in p:
        s.remove(i)
    s=lexicographi_sort(s)
    #print(s)
    st=''
    for i in s:
        st+=i
    for i in range(len(s)):
        if flag==-1:
            break
        if ord(z)>ord(s[i]) and flag!=-1:
            continue
        elif ord(z)<ord(s[i]) and flag!=-1:
            flag=-1
            print(st[:i]+p+st[i:])
            break
        elif ord(z)==ord(s[i]):
            for j in range(1,lenp):
                if ord(p[j:j+1])>ord(s[i]):
                    
                    break
                if ord(p[j:j+1])<ord(s[i]) and flag!=-1:
                    print(st[:i]+p+st[i:])
                    flag=-1
                    break
                else:
                    continue
    else:
        if flag!=-1:
            print(st+p)
        


  
            
        
    
 