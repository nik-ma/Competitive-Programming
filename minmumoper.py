for _ in range(int(input())):
    n=int(input())
    num=[int(x) for x in input().split()]
    s=set(num)
    if len(s)==1:
        print(n)
    else:
        print(1)