for _ in range(int(input())):
    n=int(input())
    num=[int(x) for x in input().split()]
    
    for i in range(n):
        print(pow(2,n-1-i,1000000007),end=" ")
    print()