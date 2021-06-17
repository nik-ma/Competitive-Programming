def getSum(n): 
   
    sum = 0
    while (n != 0): 
      
        sum = sum + int(n % 10) 
        n = int(n/10) 
      
    return sum
for _ in range(int(input())):
    n=int(input())
    monty=[]
    chef=[]
    ms=0
    cs=0
    for i in range(n):
        c,m=map(int,input().split())
        monty.append(m)
        chef.append(c)
    for k in range(n):
        mos=getSum(monty[k])
        cos=getSum(chef[k])
        if mos>cos:
            ms+=1
        elif cos>mos:
            cs+=1
        else:
            ms+=1
            cs+=1
    if ms>cs:
        print(1,ms)
    elif cs>ms:
        print(0,cs)
    else:
        print(2,ms)
