for _ in range(int(input())):
    x,y,z=map(int,input().split())
    if x==y and y==z:
        print('YES')
        print(x,x,x)
        continue
    elif x>=y and z!=y:
        print('NO')
    else:
        print('YES')
        print(x,y,z)