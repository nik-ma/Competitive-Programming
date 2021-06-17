for _ in range(int(input())):
    n=int(input())
    num=list(map(int,input().split()))
    for i in num:
        if i%2==0:
            print("NO")
            break
    else:
        print("YES")