import sys

def countOne(n): 

    count = 0

    while (n): 

        n = n & (n - 1) 

        count += 1

  

    if (count % 2 == 0): 
        return 1
    else: 
        return 0
for i in range(int(sys.stdin.readline())):
    n,q=map(int,sys.stdin.readline().split())
    a=[int(i) for i in sys.stdin.readline().split()]
    p=[]
    l=[]
    query=[]
    for i in range(q):
        query.append(int(sys.stdin.readline()))
    for i in range(n):
        p.append(countOne(a[i]))
    for i in range(q):
        l.append(countOne(query[i]))
    ce=p.count(1)
    co=p.count(0)
    print(ce,co,p,l)
    for i in range(q):
        if l[i]:
            co=co
            ce=ce
        else:
            ce,co=co,ce    
        print(ce,co)

    