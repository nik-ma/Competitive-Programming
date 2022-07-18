from collections import defaultdict
class Solution:
    def subarraySum(self, nums: List[int], k: int) -> int:
        dicti=defaultdict(lambda :0)
        n=len(nums)
        sumt=0
        pre=[]
        ans=0
        for i in range(n):
            sumt+=nums[i]
            if sumt-k in dicti:
                ans+=dicti[sumt-k]
            if sumt-k==0:
                ans+=1
            dicti[sumt]+=1
    
        return ans
            
        
        
        
            