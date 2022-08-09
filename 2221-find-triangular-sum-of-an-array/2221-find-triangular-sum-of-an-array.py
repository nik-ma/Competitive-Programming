class Solution:
    def triangularSum(self, nums: List[int]) -> int:
        result = 0
        m = len(nums) - 1
        mCk = 1
        for k, num in enumerate(nums):
            result = (result + mCk * num) % 10
            mCk *= m - k
            mCk //= k + 1
        return result
            