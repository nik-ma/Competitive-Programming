n=int(input())
arr=[]
for i in range(n):
    x,h=map(int,input().split())
    arr.append([x,h])

q=int(input())
for _ in range(q):
    l,r,he=map(int,input().split())
    count=0
    for i in range(len(arr)):
        try:
            #print(arr[i][1],arr[i][0],arr[])
            if arr[i][1]==he and arr[i][0]>=l and arr[i][0]<=r:
                #print('hello')
                arr.pop(i)
                #print(arr)
                count+=1
        except:
            pass
    print(count)
    
    