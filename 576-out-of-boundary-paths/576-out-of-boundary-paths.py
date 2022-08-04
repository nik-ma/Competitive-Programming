class Solution:
    def findPaths(self, m: int, n: int, maxMove: int, startRow: int, startColumn: int) -> int:
        # ans=0
        m,n=n,m
        dp={}
        def solve(i,j,k):
            # nonlocal ans
            if k<0:
                return 0
            if (i<0 or i>n-1 or j<0 or j>m-1):
                return 1
            if (i,j,k) in dp:
                return dp[(i,j,k)]
            ans=0
            ans+=solve(i+1,j,k-1)
            ans+=solve(i-1,j,k-1)
            ans+=solve(i,j+1,k-1)
            ans+=solve(i,j-1,k-1)
            # ans+=pt
            dp[(i,j,k)]= ans%(10**9+7)
            return dp[(i,j,k)]
        return solve(startRow,startColumn,maxMove)
        
        
            