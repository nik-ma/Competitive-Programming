class Solution:
  def permute(self, nums: List[int]) -> List[List[int]]:
    ans=[]
    def solve(ind,res,vis):
        if len(res)==len(nums):
            ans.append(res[:])
            return 
        if len(res)>len(nums):
            return
        for i in range(len(nums)):
            if i not in vis:
                vis.add(i)
                solve(i,[nums[i]]+res,vis)
                vis.remove(i)
                
                
                
    solve(0,[],set())
    return ans