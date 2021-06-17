import math
for _ in range(int(input())):
    a,b,c=map(int,input().split())
    p,q,r=map(int,input().split())
    if a==0 or b==0 or c==0:
        break
    m=[p-a,q-b,r-c]
    n=[p/a,q/b,r/c]
    if a==p and b==q and c==r:
        print(0)
        continue
    if (m[0]==m[1] and m[1]==m[2])or (n[0]==n[1] and n[1]==n[2] and (n[0]==math.floor(n[0]) and math.floor(n[1]==n[1]) and n[2]==math.floor(n[2]))):
        print(1)
        continue
    k=m.count(0)
    if k==2:
        print(1)
        continue
    if ((n[0]==n[1] and m[2]==0) or (n[1]==n[2]and m[0]==0) or (n[0]==n[2] and m[1]==0) and (n[0]==math.floor(n[0]) and math.floor(n[1]==n[1]) and n[2]==math.floor(n[2]))):
        print(1)
        continue
    

          

                    



