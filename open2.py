for _ in range(int(input())):
    n = int(input())
    tg = [int(i) for i in input().split()]
    tz = [int(j) for j in input().split()]
    tg.sort()
    tz.sort()
   # print(tg)
   # print(tz)
    count=0
    k=0
    mo=0
    while k<=n-1:
        if tg[k]>tz[mo]:
            count+=1
            mo+=1
            k+=1
        else:
            m=k
            for l in range(m+1,n):
                if tg[l]>tz[mo]:
                    #tg[l],tg[k]=tg[k],tg[l]
                    k=l+1
                    count+=1
                    break
            else:
                k+=1
            mo+=1
    print(count)

