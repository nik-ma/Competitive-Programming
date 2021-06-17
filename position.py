
T =int(input())
for i in range(T):
    positive=[0]*10000000000

    n =int(input())
    
    position =[]

    matrix=[]
    for j in range(n):
        pos,vel=map(int,input().split())
        position.append(100000+pos)
        positive[100000+pos]=vel
    sort(position)
    prev=-1000000
    strjn="POSSIBLE"
    for i in position:
        if positive[i]<prev:
            stjr="NOT POSSIBLE"
            break
print(strjn)







