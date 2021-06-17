#for ten points lol
n,q=map(int,input().split())
h=[int(x) for x in input().split()]
a=[int(x) for x in input().split()]
impossible=set()
for i in range(q):
    taste=0
    flag=0
    s,t,v=map(int,input().split())
    if t==v:
        print(a[t-1])
        continue
    if s==1:
        a[t-1]=v
        continue
    elif (t,v) in impossible:
        print(-1)
        continue
    else:
       # if 
        if t>v:
            
            for k in range(t-2,v-2,-1):
                if h[t-1]>h[k]:
                    continue
                else:
                    print(-1)
                    flag=1
                    break
        elif t<v:
            for k in range(t,v):
                if h[t-1]>h[k]:
                    continue
                else:
                    print(-1)
                    flag=1
                    break
        else:
            taste=a[t-1]
            print(taste)
            continue
        if flag!=1:
            for ji in range(t,n):
                impossible.add((v,ji))
            for ji in range(v,t):
                impossible.add((ji,t))
            for ji in range(v,t):
                impossible.add((ji,t)) 
           
            
            if t>v:
                pre=[-1]
                j=0
                for i in range(v-1,t):
                    #print('hey')
                    if pre[j]<h[i]:
                        taste+=a[i]
                        # print('hey in if ')
                        j+=1
                        pre.append(h[i])
                    else:
                       # print('hey in ekse')
                        pre.append(pre[j])
                        j+=1
            else:
                pre=[-1]
                j=0
                for i in range(v-1,t-2,-1):
                   #print('hey') 
                    if pre[j]<h[i]:
                        taste+=a[i]
                       # print('hey in if ')
                        j+=1
                        pre.append(h[i])
                    else:
                        # print('hey in ekse')
                        pre.append(pre[j])
                        j+=1
            print(taste)
    print(impossible)
    