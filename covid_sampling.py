import sys
def covid(n):
    ans = [[-1]*n for i in range(n)]
    if True:

        for i in range(0,n,2):
            print(1,i+1,1,i+2,n)
            temp=int(input())
            for j in range(n-1,n//2-1,-1):
                print(1,i+1,1,i+2,j)
                x=int(input())
                if temp-x==0:
                    ans[i][j]=0
                    ans[i+1][j]=0
                    temp=x
                    continue
                if temp-x==2:
                    ans[i][j]=1
                    ans[i+1][j]=1
                    temp=x
                    continue
                else:
                    print(1,i+1,n,i+1,n)
                    y=int(input())
                    if y==0:
                        ans[i][n-1]=0
                        ans[i+1][n-1]=1
                    else:
                        ans[i][n-1]=1
                        ans[i+1][n-1]=0                 
            print(1,i+1,1,i+2,n)
            temp=int(input())
            for j in range(2,n//2+2):
                print(1,i+1,j,i+2,n)
                x=int(input())
                if temp-x==0:
                    ans[i][j-2]=0
                    ans[i+1][j-2]=0
                    temp=x
                    continue
                if temp-x==2:
                    ans[i][j-2]=1
                    ans[i+1][j-2]=1
                    temp=x
                    continue
                else:
                    print(1,i+1,1,i+1,1)
                    y=int(input())
                    if y==0:
                        ans[i][0]=0
                        ans[i+1][0]=1
                    else:
                        ans[i][0]=1
                        ans[i+1][0]=0    
  
            
           
    print(2)
    for i in ans:
        print(*i)
    if int(input())==1:
        return
    else: 
        sys.exit()
    
    
for _ in range(int(input())):
    n,p = map(int,input().split())
    covid(n)