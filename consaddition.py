
testcases=vary(1)
for _ in range(testcases):
    r,c,x=vary(3)
    a=[]
    for i in range(r):
        a.append(array_int())
    b=[]
    for i in range(r):
        b.append(array_int())
    copy=[[0]*(c+1) for i in range(r+1)]
    if 1:
        if r*c*x<10**5:
            for i in range(r):
                for j in range(c-x+1):
                    swapping=b[i][j]-a[i][j]
                    a[i][j]+=(swapping)
                    for k in range(1,x):
                        a[i][j+k]+=(swapping)
                    
            for i in range(x-1):
                for j in range(r-x+1):
                    swapping=b[j][c-1-i]-a[j][c-1-i]
                    a[j][c-1-i]+=(swapping)
                    for k in range(1,x):
                        a[j+k][c-1-i]+=(swapping)
        else:
            for i in range(r):
                swapping=0
                ct=0
                for j in range(c-x+1):
                    if j-x>=0:
                        swapping-=copy[i][j-x]
                    a[i][j]+=(swapping)
                    pt=b[i][j]-a[i][j]
                    copy[i][j]=pt
                    swapping+=copy[i][j]
                    a[i][j]=pt
                    
                for k in range(c-x+1,c):
                    a[i][k]+=swapping
                    
            copy=[[0]*(c+1) for i in range(r+1)]
            for i in range(c-x+1,c):
                swapping=0
                for j in range(0,r-x+1):
                    if j-x>=0:
                        swapping-=copy[j-x][i]
                    a[j][i]+=swapping
                    pt=b[j][i]-a[j][i]
                    copy[j][i]=pt
                    swapping+=copy[j][i]
                    a[i][j]=pt
                for k in range(r-x+1,r):
                    a[k][i]+=swapping
    
    signature=0
    for j in range(x-1):
        for i in range(x-1):
            if a[r-1-j][c-1-i]!=b[r-1-j][c-1-i]:
                signature=1
                    
    if signature==1:
        print('No')
    else:
        print('Yes')        
        
