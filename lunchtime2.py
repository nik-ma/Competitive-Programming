#weird distance 
for _ in range(int(input())):
    n=int(input())
    a=[int(i) for i in input().split()]
    b=[int(i) for i in input().split()]
    sum_a=0
    sum_b=0
    weirdd=0
    for i in range(n):
        if sum_a==sum_b and sum_a+a[i]-sum_a==sum_b+b[i]-sum_b:
            weirdd+=sum_a+a[i]-sum_a
        sum_a+=a[i]
        sum_b+=b[i]
    print(weirdd)



