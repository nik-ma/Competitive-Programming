
testcases=vary(1)
for _ in range(testcases):
    n,m=vary(2)
    arr=[]
    for _ in range(n):
        arr.append([i for i in input()])
    first=1
    val=[[-1]*m for i in range(n)]
    for i in range(n):
        for j in range(m):
            val[i][j]=arr[i][j]
    data=1
    for i in range(n):
        if first==0:
            break
        for j in range(m):
            if arr[i][j]=='R' and data==1:
                pass
            elif arr[i][j]=='W' and data==1:
                first=0
                break
            elif arr[i][j]=='R' and data==0:
                first=0
                break
            elif arr[i][j]=='W' and data==0:
                pass
            else:
                if data==1:
                    arr[i][j]='R'
                else:
                    arr[i][j]='W'
            if j==m-1:
                    if j%2==0:
                        data^=1
                    else:
                        continue
            else:
                data^=1
            # data^=1
        # data^=1
    if first==1:
        print('YES')
        for i in range(n):
            for j in range(m):
                print(arr[i][j],end="")
            print()
    else:
        second=1
        data=1
        arr=val
        # print(arr)
        for i in range(n):
            if second==0:
                break
            for j in range(m):
                if arr[i][j]=='W' and data==1:
                    pass
                elif arr[i][j]=='R' and data==1:
                    second=0
                    break
                elif arr[i][j]=='W' and data==0:
                    second=0
                    break
                elif arr[i][j]=='R' and data==0:
                    pass
                else:
                    if data==1:
                        arr[i][j]='W'
                    else:
                        arr[i][j]='R'
                if j==m-1:
                    if j%2==0:
                        data^=1
                    else:
                        continue
                else:
                    data^=1

                    
            # data^=1
        
        if second==1:
            print('YES')
            for i in range(n):
                for j in range(m):
                    print(arr[i][j],end="")
                print() 
        else:
            print('NO')


