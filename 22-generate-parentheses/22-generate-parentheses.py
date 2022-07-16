
class Solution:
    def generateParenthesis(self, n: int) -> List[str]:
        ans=[]
        def helper(op,cl,current):
            if op==cl==n:
                ans.append(current)
            if op<n:
                helper(op+1,cl,current+'(')
            if cl<op and cl<n:
                helper(op,cl+1,current+')')
        helper(0,0,'')
        
        return ans
        
    
        
    