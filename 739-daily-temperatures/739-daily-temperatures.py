class Solution:
    def dailyTemperatures(self, temperatures: List[int]) -> List[int]:
        stack=[]
        n=len(temperatures)
        ans=[0]*n
        for i in range(n-1,-1,-1):
            while stack and temperatures[stack[-1]]<=temperatures[i]:
                stack.pop()
            # print(stack)
            if len(stack)>0:
                ans[i]=stack[-1]-i
            
            stack.append(i)
            # print(stack)
        return ans