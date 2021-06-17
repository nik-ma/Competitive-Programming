# cook your dish here
import sys 
import math
  
# Returns the minimum value of the  
# difference of the two sets. 
def findMin(a, n): 
      
    su = 0
      
    # Calculate sum of all elements  
    su = sum(a) 
  
    # Create an 2d list to store  
    # results of subproblems 
    dp = [[0 for i in range(su + 1)]  
             for j in range(n + 1)] 
  
    # Initialize first column as true. 
    # 0 sum is possible  
    # with all elements.  
    for i in range(n + 1): 
        dp[i][0] = True
          
    # Initialize top row, except dp[0][0], 
    # as false. With 0 elements, no other  
    # sum except 0 is possible 
    for j in range(1, su + 1): 
        dp[0][j] = False
      
    # Fill the partition table in  
    # bottom up manner 
    for i in range(1, n + 1): 
        for j in range(1, su + 1): 
              
            # If i'th element is excluded  
            dp[i][j] = dp[i - 1][j] 
              
            # If i'th element is included 
            if a[i - 1] <= j: 
                dp[i][j] |= dp[i - 1][j - a[i - 1]] 
      
    # Initialize difference  
    # of two sums. 
    diff = sys.maxsize 
  
    # Find the largest j such that dp[n][j]  
    # is true where j loops from sum/2 t0 0  
    for j in range(su // 2, -1, -1): 
        if dp[n][j] == True: 
            diff = su - (2 * j) 
            break
              
    return diff
def find_partition(int_list):
    "returns: An attempt at a partition of `int_list` into two sets of equal sum"
    A = set()
    B = set()
    tt=sum(A)
    tt2=sum(B)
    for n in sorted(int_list, reverse=True):
        if tt < tt2:
            A.add(n)
            tt+=n
        else:
            B.add(n)
            tt2+=n
    return [A, B]
k=int(input())
for _ in range(int(input())):
    n=int(input())
    t1=0
    t2=0
    if k==2:
        num=[int(i*i) for i in range(1,n+1)]
    if k==1:
        num=[int(i) for i in range(1,n+1)]
    total=sum(num)
    arr=find_partition(num)
    first=arr[0]
    second=arr[1]
    # print(first)
    # print(second)
    ans=[0]*n
    tt=0
    for i in first:
        tt+=i
        ans[int(math.sqrt(i))-1]=1
    print(abs((total-tt)-tt))
    for i in ans:
        print(i,end="")
    print()

    

    
    """ if k==1:
        num=[int(i) for i in range(1,n+1)]
        t2=sum(num)//2
        num2=[0]*n
        for i in range(n-1,-1,-1):
            if t2>=t1+num[i]:
                t1+=num[i]
                num2[i]='1'
        print(abs((sum(num)-t2)-t1))
    
    
        
        for i in range(n):
            print(num2[i],end="")
        print()
    if k==2:
        num=[int(i*i) for i in range(1,n+1)]
        t2=sum(num)//2
        num2=[0]*n
        t3=sum(num)-t2
        for i in range(n):
            if t3<t1+num[i]:
                t1+=num[i]
                num2[i]='1'
        print(abs(t2+(t3-t1)-t1))

    
        
        for i in range(n):
            print(num2[i],end="")
        print()  """
    
