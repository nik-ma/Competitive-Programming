class Solution:
    def subsetsWithDup(self, nums: List[int]) -> List[List[int]]:
        res=[]
        n=len(nums)
        st=set()
        def solve(i,ans):
            if i>n:
                return 
            if i==n:
                # ans.append(nums[i])
                if tuple(sorted(ans)) not in st:
                    
                    res.append(ans[:])
                    st.add(tuple(sorted(ans)))
                return 
                # ans.pop()
            solve(i+1,ans)
            ans.append(nums[i])
            solve(i+1,ans)
            ans.pop()
            return
        solve(0,[])
        return res
                
        