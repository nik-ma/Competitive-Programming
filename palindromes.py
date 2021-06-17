for i in range(int(input())):
    n=int(input())
    s=[i for i in input()]
    c=0
    for i in range(n//2-1):
        if s[i]==s[n-i-1]:

            continue
        else:
            if s[i]!=s[n-1-i]:
                if s[i]!=s[n-1-i-1]:
                    print('NO')
                    c=-1
                    break
            else:
                c+=1
                
                continue
    if c!=-1:
        print("YES")
        print(c)
