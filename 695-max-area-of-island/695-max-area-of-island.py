
from collections import deque
class Solution:
    def maxAreaOfIsland(self, grid: List[List[int]]) -> int:

        q=deque()
        n=len(grid)
        m=len(grid[0])
        
        vis=set()
        maxi=0
        def dfs(i,j,ans):
            ans[0]+=1
            vis.add((i,j))
            for x,y in [[-1,0],[0,1],[1,0],[0,-1]]:
                if x+i>=0 and x+i<n and y+j>=0 and y+j<m  and (x+i,y+j) not in vis and grid[x+i][y+j]==1:
                    vis.add((x+i,y+j))
                    dfs(x+i,y+j,ans)
                    
            
                    
        for i in range(n):
            for j in range(m):
                if grid[i][j]==1 and (i,j) not in vis:
                    ans=[0]
                    dfs(i,j,ans)
                    maxi=max(ans[0],maxi)
                    
        return maxi