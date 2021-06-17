from collections import Counter
for _ in range(int(input())):
    n,c,k=map(int,input().split())
    listu=[0 for i in range(n)]
    i=0
    while i<n:
        a,b,listu[i]=map(int,input().split())
        i+=1
    costu=[int(x) for x in input().split()]
    dictionaryt=dict(Counter(listu))
    listi=[]
    for i in dictionaryt:
        listi.append(dictionaryt[i])
    if costu[0]==0:
        print(0)
        continue
    i=0
    while k-costu[0]>=0:
        listi[listi.index(max(listi))]-=1
        k-=costu[0]
    answer=0
    for i in listi:
        answer+=(i*(i-1)*(i-2))//6
    print(answer)
