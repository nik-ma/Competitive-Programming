class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        n=len(prices)
        @cache
        def solve(i,prev,k):
            if i==n or k==0:
                return 0
            nottake=solve(i+1,prev,k)
            if prev==1:
                take=-prices[i]+solve(i+1,prev^1,k)
                # nottake=solve(i+1,prev,k)
            else:
                take=solve(i+1,prev^1,k-1)+prices[i]
                
            return max(take,nottake)
        return solve(0,1,2)
                
            
        