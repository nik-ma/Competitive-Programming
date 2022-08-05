class Solution:
    def combinationSum4(self, nums: List[int], target: int) -> int:
        # nums+=nums
        n=len(nums)

        nums.sort()
        ans=0
        k=sum([target%i==0 for i in nums])
        @cache
        def solve(i,target):
            # nonlocal ans
            if target==0:
                return 1
            if target<0:
                return 0
            # nottake=solve(i+1,target)
            take=0
            for j in range(n):
                
                    take+=solve(j,target-nums[j])
            return take
        return solve(0,target)
        # print(ans)