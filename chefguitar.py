for _ in range(int(input())):
    n=int(input())
    tones=[int(x) for x in input().split()]
    sum=0
    for i in range(n-1):
        sum+=abs(tones[i]-tones[i+1])-1
    print(sum)
