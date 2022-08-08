class Solution:
    def lengthOfLIS(self, nums: List[int]) -> int:
        subarray=[float(-inf)]
        n=len(nums)
        for i in range(n):
            if nums[i]>subarray[-1]:
                subarray.append(nums[i])
            elif nums[i]==subarray[-1]:
                continue
            else:
                ind=bisect.bisect_left(subarray,nums[i])
                if ind>len(subarray)-1:
                    subarray.append(nums[i])
                    continue
                subarray[ind]=nums[i]
        # print(subarray)
        return len(subarray)-1
                
                