for _ in range(int(input())):
    n=int(input())
    arr=list(map(int,input().split()))
    arr2=set(arr)
    new=[]
    for i in arr:
        if i in arr2:
            new.append(i)
            arr2.remove(i)
    print(*new)
