class Solution:
    def combinationSum(self, candidates: List[int], target: int) -> List[List[int]]:
        ans=[]
        candidates.sort()
        n=len(candidates)
        def solve(ind,target,res):
            if target<0:
                return 
            if target==0:
                ans.append(res)
                return
            if ind>n-1:
                return
            solve(ind+1,target,res)
            solve(ind,target-candidates[ind],res+[candidates[ind]])
                # solve(ind+1,target-candidates[i],res)
                # res.remove(candidates[i])
        solve(0,target,[])
        return ans
                