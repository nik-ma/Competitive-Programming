class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        if len(nums)==0:
            return 0
        # nums=list(set(nums))
        # nums.sort()
        nums=set(nums)
        maxi=1
        for i in nums:
            if i-1 not in nums:
                before=i
                after=i
                ans=1
                while after+1 in nums:
                    ans+=1
                    after+=1
                maxi=max(maxi,after-before+1)
        return maxi
            
                
        
                