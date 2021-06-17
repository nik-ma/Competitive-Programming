for _ in range(int(input())):
    n=int(input())
    if n==2:
        print(1)
        continue
    if n%2==0:
        print(n//2)
    else:
        print(n//2+1)