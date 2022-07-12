class Solution:
    def subsets(self, nums: List[int]) -> List[List[int]]:
        ans=[]
        n=len(nums)
        def solve(ind,res):
            if ind>n:
                return
            if ind>n-1:
                ans.append(res)
                return
            solve(ind+1,res)
            solve(ind+1,[nums[ind]]+res)
        solve(0,[])
        return ans
            
            
        