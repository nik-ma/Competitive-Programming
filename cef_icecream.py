for _ in range(int(input())):
    n=int(input())
    price = [int(i) for i in input().split()]
    conis={'5':0,'10':0,'15':0}
    for i in price:
        if i-5==0:
            conis[str(i)]+=1
        elif i-5==5:
            if conis[str(5)]!=0:
                conis[str(5)]-=1
                conis[str(10)]+=1
            else:
                print('NO')
                break
        elif i-5==10:
            if conis[str(10)]!=0:
                conis[str(10)]-=1
                conis[str(15)]+=1
            elif conis[str(5)]>=2:
                conis[str(5)]-=2
                conis[str(15)]+=1
            else:
                print('NO')
                break
    else:
        print('YES')
                
                



    