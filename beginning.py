s='helloworld'
c=0
for i in range(int(input())):
    beg=input()
    
    for i in beg:
        if i in s:
            continue
        else:
            c=2
            print('NO')
    if c!=2:
        print("YES")
