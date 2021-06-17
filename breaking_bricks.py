tc=int(input())
k=tc
l=[]
while tc:
    
    s,w1,w2,w3=map(int,input().split())
    z=w1+w2+w3
    if s>=z:
        l.append(1)
    elif (s>=w1+w2 or s>=w2+w3) and s<z:
        l.append(2)
    else:
        l.append(3)
   
    tc-=1
for i in range(k):
    print(l[i])