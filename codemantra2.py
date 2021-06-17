for _ in range(int(input())):
    s,t=map(str,input().split())
    p=''
    q=''
    for i  in s:
        if i!=',':
            p+=i
    for i in t:
        if i!=',':
            q+=i
    if p==q:
        print('equal')
    else:
        print('different')