for _ in range(int(input())):
    n=int(input())
    sx=[]
    sy=[]
    dic_x={}
    dic_y={}
    for i in range(4*n-1):
        x,y=map(int,input().split())
        sx.append(x)
        sy.append(y)
    for i in sx:
        if str(i) in dic_x:
            dic_x[str(i)]+=1
        else:
            dic_x[str(i)]=1
    for i in sy:
        if str(i) in dic_y:
            dic_y[str(i)]+=1
        else:
            dic_y[str(i)]=1
    sxs=set(sx)
    sys=set(sy)
    for i in sxs:
        if dic_x[str(i)]%2!=0:
            mpx=i
            break
    for i in sys:
        if dic_y[str(i)]%2!=0:
            mpy=i
            break
    print(mpx,mpy)
