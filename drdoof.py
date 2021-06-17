def next(arr, target): 
    start = 0; 
    end = len(arr) - 1; 
  
    ans = -1; 
    while (start <= end): 
        mid = (start + end) // 2; 
  
        # Move to right side if target is 
        # greater. 
        if (arr[mid] <= target): 
            start = mid + 1; 
  
        # Move left side. 
        else: 
            ans = mid; 
            end = mid - 1; 
  
    return ans; 
for _ in range(int(input())):
    n=int(input())
    num=list(map(int,input().split()))
    num.sort()
    num2=set(num)
    q=int(input())
    for i in range(q):
        x,y=map(int,input().split())
        xnew=x+y
        count=0
        if xnew in num2:
            print(-1)
        else:
            t=next(num,xnew)
            if t==-1:
                print(n)
            elif t==0:
                print(0)
            else:
                print(t)

                    