class Solution:
    def lengthOfLIS(self, nums: List[int]) -> int:
        n=len(nums)
        dp=[1]*(n+1)
        for i in range(1,n):
            maxi=-1
            for j in range(i):
                if nums[j]<nums[i] and maxi<dp[j]:
                    dp[i]=dp[j]+1
                    maxi=dp[j]
        return max(dp)