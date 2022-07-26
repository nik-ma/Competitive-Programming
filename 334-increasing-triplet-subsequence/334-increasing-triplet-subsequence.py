class Solution:
    def increasingTriplet(self, nums: List[int]) -> bool:
        
        first = second = float('inf')
        for n in nums:
            if n <= first:
                first = n
            elif n <= second:
                second = n
            else:
                return True
        return False
#         dp={}
#         def solve(ind,k,prev):
#             if k==0:
#                 dp[(ind,k)]=True
#                 return True
#             if ind==0 and k==1:
#                 dp[(ind,k)]=nums[ind]<prev
#                 return dp[(ind,k)]
#             if ind<0:
#                 dp[(ind,k)]=False
#                 return False
#             if (ind,k) in dp:
#                 return dp[(ind,k)]
                
            
#             nottake=solve(ind-1,k,prev)
#             take=False
#             if nums[ind]<prev:
#                 take=solve(ind-1,k-1,nums[ind])
#             dp[(ind,k)]= take or nottake
#             return dp[(ind,k)]
#         return solve(len(nums)-1,3,float('inf'))
            
            