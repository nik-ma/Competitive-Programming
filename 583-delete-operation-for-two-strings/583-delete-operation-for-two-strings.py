class Solution:
    def minDistance(self, word1: str, word2: str) -> int:
        @cache
        def solve(i,j):
            if i<0:
                return j+1
            if j<0:
                return i+1
            if word1[i]==word2[j]:
                return solve(i-1,j-1)
            return min(1+solve(i-1,j),1+solve(i,j-1))
        return solve(len(word1)-1,len(word2)-1)