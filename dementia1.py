for _ in range(int(input())):
    n=int(input())
    num=[int(x) for x in input().split()]
    if (len(num)==1):
        print("first")
        continue
    if len(num)==2:
        if num[0]!=num[1]:
            print("first")
            continue
        else:
            print("draw")
            continue
    sum_a=0
    sum_b=0
    num.sort(reverse=True)
    sum_a+=num[0]
    sum_b+=num[1]+num[2]

    for i in range(3,n):
        if i%2!=0:
            sum_a+=num[i]
        else:
            sum_b+=num[i]
        
    if sum_a>sum_b:
        print('first')
    elif sum_b==sum_a:
        print("draw")
    else:
        print('second')
    #print(sum_a,sum_b)