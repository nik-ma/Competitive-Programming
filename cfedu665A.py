for _ in range(int(input())):
    n=int(input())
    num=[int(x) for x in input().split()]
    s=num[0]+num[1]
    #print(s)
    for i in range(2,n):
        #print(num[i])
        if s<=num[i]:
            print(1,2,i+1)
            break
    else:
        print(-1)

