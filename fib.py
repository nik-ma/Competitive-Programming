n = int(input())

if n>=5:
    exp =1
    countr =0
    ans = 0
    while exp <= n:
        exp *= 5
        countr+=1
    for i in range(1,countr+1):
        ans += n//(5**i)

else:
    ans =0


print(ans)
