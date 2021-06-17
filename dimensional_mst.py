def dist(i,j,points):
    ans=0
    # print(points[i],points[j])
    for ai,bi in zip(points[i],points[j]):
        ans+=(abs(ai-bi))
    # print(ans)
    return ans

if 1:
    n,d=[int(c) for c in input().split()]
    points=[]
    for i in range(n):
        a=[int(c) for c in input().split()]
        points.append(a)
    
    
    ## d stores the maximum distance of the node i from the farthest node present in the tree

    present=[False for i in range(n)]
    present[0]=True
    d=[dist(0,i,points) for i in range(n)]
    ans=0
    # mod=747474747
    for ite in range(1,n):
        j=0
        for i in range(n):
            if (not present[i]) and (j == 0 or d[j] < d[i]) :
                j=i
        present[j] = True

        if d[j] <= 1:
            break
        else:
            ans=ans+(d[j]) 
            
        
        
        for i in range(n):
            if present[i] == False:
                d[i] = max(d[i],dist(i,j,points))

    print(ans)
        
        