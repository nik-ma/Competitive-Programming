arr=[3,2,4,7,8,3,21,23]
tt=arr[0]
for i in range(1,len(arr)):
    tt^=arr[i]
print(tt)

arr2=[2**i for i in range(20)]
tt=[]
for i in arr2:
    sumt=0
    for j in arr: 
        sumt+=j^i
    tt.append(sumt)
print(tt)

