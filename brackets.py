for _ in range(int(input())):
    n=int(input())
    s=input()
    ob=0
    cb=0
    count=0
    for i in s:
        if i=='(':
            ob+=1
        elif i==')':
            cb+=1
        if cb>ob:
            count+=1
            cb=0
            ob=0
    print(count)
