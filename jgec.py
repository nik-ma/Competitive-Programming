for _ in range(int(input())):
    n=int(input())
    arr=input()
    
    count=0
    
    for i in range(len(arr)-3):
        if arr[i]=="J":
            if arr[i+1]=="G":
                if arr[i+2]=="E":
                    if arr[i+3]=="C":
                        count+=1
    print(count)