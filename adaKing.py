for _ in range(int(input())):
    k=int(input())
    y=64
    a=['O']
    for i in range(1,k):
        a.append('.')
    for j in range(k,64):
        a.append('X')
    arr=[]
    i=0
    while i<64:
        arr.append(a[i:i+8])
        i+=8
    for i in range(8):
        if i%2==0:
            for j in range(8):
                print(arr[i][j],end="")
            print()
        else:
            for j in range(7,-1,-1):
                print(arr[i][j],end="")
            print()