def mergesort(array,start,end):
    if start==end:

        return array[start:end+1]
    else:
        mid=(start+end)//2
        arr1=mergesort(array,start,mid)
        arr2=mergesort(array,mid+1,end)
        i=0
        j=0
        k=0
        print(arr1,arr2)
        while i<len(arr1) and j<len(arr2):
            print(arr1,arr2)
            print(i,j)
            if i==len(arr1) or j==len(arr2):
                if i==len(arr1):
                    array[start+k]=arr2[j]
                    j+=1
                else:
                    array[start+k]=arr1[i]
                    i+=1
            
            else:

                if arr1[i]<arr2[j]:
                    array[start+k]=arr1[i]
                    if i<len(arr1):
                        i+=1


                else:
                    array[start+k]=arr2[j]
                    if j<len(arr2):
                        j+=1


            k+=1
        return array[start:end+1]


array=[int(i) for i in input().split()]
mergesort(array,0,len(array)-1)
print(array)

