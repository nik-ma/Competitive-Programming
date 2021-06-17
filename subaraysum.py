#Python3 code to compute  
# sum of subarray elements 
  
#function compute sum  
# all sub-array 
def SubArraySum(arr, n ): 
    result = 0
  
    # computing sum of subarray  
    # using formula 
    for i in range(0, n): 
        result = (arr[i] * (i+1) * (n-i)) 
        print(result)
  
    # return all subarray sum 
    return result  
  

for _ in range(int(input())):
    s=input()
    arr=[int(x) for x in s]
  
    
    n = len(arr) 
    print(SubArraySum(arr,n))