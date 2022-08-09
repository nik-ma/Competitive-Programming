class Solution:
    def kthSmallestPath(self, destination: List[int], k: int) -> str:
        from math import comb
        r, c = destination
        
        ret = []
        remDown = r
        for i in range(r + c):
            remSteps = r + c - (i + 1)
            com = comb(remSteps, remDown)
            if com >= k:
                ret.append("H")
            else:
                remDown -= 1
                k -= com
                ret.append("V")
                
        return ''.join(ret)