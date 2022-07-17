class Solution:
    def queensAttacktheKing(self, queens: List[List[int]], king: List[int]) -> List[List[int]]:
        ans=[]
        n=8
        m=8
        x,y=king[0],king[1]
        i=1
        while x-i>=0:
            if [x-i,y] in queens:
                ans.append([x-i,y])
                break
            i+=1
        i=1
        while x+i<n:
            if [x+i,y] in queens:
                ans.append([x+i,y])
                break
            i+=1
        i=1
        while y-i>=0:
            if [x,y-i] in queens:
                ans.append([x,y-i])
                break
            i+=1
        i=1
        while y+i<m:
            if [x,y+i] in queens:
                ans.append([x,y+i])
                break
            i+=1
        i=1
        while y-i>=0 and x-i>=0:
            if [x-i,y-i] in queens:
                ans.append([x-i,y-i])
                break
            i+=1
        i=1
        while y+i<m and x+i<n:
            if [x+i,y+i] in queens:
                ans.append([x+i,y+i])
                break
            i+=1
        i=1
        while y-i>=0 and x+i<n:
            if [x+i,y-i] in queens:
                ans.append([x+i,y-i])
                break
            i+=1
        i=1
        while y+i<m and x-i>=0:
            if [x-i,y+i] in queens:
                ans.append([x-i,y+i])
                break
            i+=1
        return ans
        