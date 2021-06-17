for _ in range(int(input())):
    s,n,k,r=map(int,input().split())
    sum = (k*(r**n-1))//(r-1)
    poss=0
    imposs=0
    if sum>s:
        print('IMPOSSIBLE',sum-s)
        poss+=sum-s
    else:
        imposs+=s-sum
        print('POSSIBLE',s-sum)
if poss<imposs:
    print('IMPOSSIBLE')
else:
    print('POSSIBLE')