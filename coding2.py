import string
arrn=[]
def subArraySum(arr, n, sum,arrn): 
      
    # Pick a starting  
    # point 
    for i in range(n): 
        curr_sum = arr[i] 
      
        # try all subarrays 
        # starting with 'i' 
        j = i + 1
        while j <= n: 
          
            if curr_sum == sum: 
                #print ("Sum found between") 
                #print("indexes % d and % d"%( i, j-1)) 
                arrn.append(i)
                arrn.append(j-1)
                
                  
            if curr_sum > sum or j == n: 
                break
              
            curr_sum = curr_sum + arr[j] 
            j += 1
  
    print ("No subarray found") 
    return 0
weight=[int(x) for x in input().split()]
dict_w={}
j=0
for i in string.ascii_lowercase[:26]:
        dict_w[i]=weight[j]
        j+=1

print(subArraySum(weight,26,9,arrn))
print(arrn[-1],arrn[-2])

