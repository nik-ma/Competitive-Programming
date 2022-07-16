class Solution:
    def findPaths(self, m: int, n: int, maxMove: int, startRow: int, startColumn: int) -> int:
        # ans=0
        m,n=n,m

        @cache
        def solve(i,j,k):
            # nonlocal ans
            if k<0:
                return 0
            
            if (i<0 or i>n-1 or j<0 or j>m-1):
                return 1

            ans=0
            ans+=solve(i+1,j,k-1)
            ans+=solve(i-1,j,k-1)
            ans+=solve(i,j+1,k-1)
            ans+=solve(i,j-1,k-1)
            # ans+=pt
            return ans%(10**9+7)
        return solve(startRow,startColumn,maxMove)
        
        
            