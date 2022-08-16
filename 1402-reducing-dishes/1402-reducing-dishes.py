class Solution:
    def maxSatisfaction(self, satisfaction: List[int]) -> int:
        satisfaction.sort()
        n=len(satisfaction)
        @cache
        def solve(ind,time):
            if ind==n:
                return 0
            nottake=solve(ind+1,time)
            take=0
            take=satisfaction[ind]*time+solve(ind+1,time+1)
            return max(take,nottake)
        return solve(0,1)