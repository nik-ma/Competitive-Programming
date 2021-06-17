flag = -1

def solve(start, end):
    #print(start,end)
    global flag
    if start<1 or start>end:
        
        return
    if start == end:
        print(start)
        x = input()
        if x== 'E':
            flag = 1
        return
        
    
    string = ""
    
    mid1 = start + (end-start)//3
    mid2 = end - (end-start)//3
    
    print(mid1)
    x1 = input()
    if x1 == 'E':
        
        flag = 1
        return
    string += x1
    
    if flag ==1:
        return
    
    print(mid1)
    x2 = input()
    string += x2
    if x1==x2:
        if x1=='L':
            return solve(start,mid1-1)
        else:
            return solve(mid1+1,end)
    if flag ==1:
        return
    
    print(mid2)
    x3 = input()
    if x3 == 'E':
        
        flag = 1
        return 
     
    string += x3
    print(mid2)
    x4 = input()
    string+= x4
    if x3==x4:
        if x3=='L':
            return solve(start,mid2-1)
        else:
            return solve(mid2+1,end)
    if flag ==1:
        return
    
    if string == "LGGL":
        return solve(mid1+1,end)
    elif string == "GLLG":
        return solve(start,mid2-1)
    
    elif string == "GLGL":
        solve(start,mid1-1)
        if flag == -1:
            solve(mid2+1,end)
    else:
        print(mid1)
        x1 = input()
        print(mid1)
        x2 = input()
        
        if x1==x2:
            if x1=='L':
                return solve(start,mid1-1)
            else:
                return solve(mid2+1,end)
        elif x1 == 'L':
            solve(start,mid1-1)
            if flag == -1:
                solve(mid2+1,end)
        
        else:
            solve(mid1+1,end)    
    
        
        
        
    
solve(1,int(input()))