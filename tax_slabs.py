def Tax(n):
    if(n<=250000):
        return 0
    elif(n<=500000):
        return 0.05*(n-250000)
    elif(n<=750000):
        return 0.1*(n-500000)+Tax(500000)
    elif(n<=1000000):
        return 0.15*(n-750000)+Tax(750000)
    elif(n<=1250000):
        return 0.2*(n-1000000)+Tax(1000000)
    elif(n<=1500000):
        return 0.25*(n-1250000)+Tax(1250000)
    else:
        return 0.3*(n-1500000)+Tax(1500000)

for _ in range(int(input())):
    totaln = int(input())
    print(totaln-int(Tax(totaln)))