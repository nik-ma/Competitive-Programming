class Solution:
    def uniquePaths(self, m: int, n: int) -> int:
        dp=[[-1]*m for i in range(n)]
        def dfs(i,j):
            if i>n-1 or j>m-1:
                return 0
            if i==n-1 and j==m-1:
                dp[i][j]=1
                return 1
            if dp[i][j]!=-1:
                return dp[i][j]
            dp[i][j]=dfs(i+1,j)+dfs(i,j+1)
            return dp[i][j]
        dfs(0,0)
        return dp[0][0]