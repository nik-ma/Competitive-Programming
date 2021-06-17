from sys import stdin,stdout
for _ in range(int(stdin.readline())):
    s=stdin.readline()
    q=int(input())
    query = [int(x) for x in stdin.readline().split()] 
    arr=[]
    ob,cb=0,0
    sec=0
    for i in s:
        
            
        if i==')' and cb==0:
            sec+=1
            continue
        elif i=="(":
            sec+=1
            cb+=1
        elif i==")" and cb!=0:
            arr.append(3)

        
        