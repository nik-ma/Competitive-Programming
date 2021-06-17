from sys import stdin,stdout
for _ in range(int(stdin.readline())):
    s=stdin.readline()
    q=int(input())
    query = [int(x) for x in stdin.readline().split()] 
    arr=[]
    for i in range(q):

        ob=0
        cb=0
        count=0
        sec=0
        for ink in s:
            if ob==cb and cb!=0:
                arr.append()
                break
            if ink=='(':
                cb+=1
                sec+=1
            elif cb==0 and ink==')':
                sec+=1
                continue
            else:
                sec+=1
                ob+=1
        else:
            stdout.writelines(str(-1)+'\n')

            

        #print(count)

