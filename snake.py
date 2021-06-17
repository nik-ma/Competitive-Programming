for _ in range(int(input())):
    r,c = map(int,input().split())

    array = []
    for i in range(r):
        array.append([int(i) for i in input().split()])

    for i in range(r):
        for j in range(c):
            if array[i][j] == 1:
                rows,cols = i,j
            if array[i][j] == 9:
                rowe,cole = i,j
    rowd = abs(rows-rowe)
    cdis = abs(cols-cole)

    if rowd > cdis:
        snk = "%.3f"%(cdis*(1.414) + rowd -cdis)
    else:
        snk = "%.3f"%(rowd*(1.414) + cdis - rowd)
   
    if int(float(snk)) == float(snk):
        snk = int(float(snk))
    else:
        snk = float(snk)
    print(snk)