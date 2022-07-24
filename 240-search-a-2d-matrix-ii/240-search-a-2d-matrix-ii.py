
import bisect
class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        
        i=0
        j=len(matrix[0])-1
        n=len(matrix)
        m=len(matrix[0])
        while j>=0 and i<n:
            if matrix[i][j]==target:
                return True
            if matrix[i][j]<target:
                i+=1
            else:
                # i+=1
                j-=1
        return False