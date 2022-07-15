class Solution:
    def minDistance(self, word1: str, word2: str) -> int:
        
        n=len((word1))
        m=len(word2)
        # @cache
        dp={}
        def solve(i,j):
            
            if i<0:
                return j+1
            if j<0:
                return i+1
            if (i,j) in dp:
                return dp[(i,j)]
            if word1[i]==word2[j]:
                dp[(i,j)]=solve(i-1,j-1)
                return dp[(i,j)]
            dp[(i,j)] = min(1+solve(i-1,j-1),1+solve(i-1,j),1+solve(i,j-1))
            return dp[(i,j)]
        return solve(n-1,m-1)