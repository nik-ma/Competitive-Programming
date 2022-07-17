class Solution:
    def letterCombinations(self, digits: str) -> List[str]:
        mapping = {'2': 'abc', '3': 'def', '4': 'ghi', '5': 'jkl', 
                   '6': 'mno', '7': 'pqrs', '8': 'tuv', '9': 'wxyz'}
        ans=[]
        def solve(ind,res):
            # print(res)
            
            if len(res)==len(digits):
                ans.append(res[:])
                return
            if ind>len(digits)-1:
                return 
            for i in (mapping[digits[ind]]):
                # solve(ind+1,i,res)
                solve(ind+1,res+i)
        if len(digits)==0:
            return []
        solve(0,'')
        return ans
        