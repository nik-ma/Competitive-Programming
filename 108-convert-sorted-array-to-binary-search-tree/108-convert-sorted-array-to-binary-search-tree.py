# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def sortedArrayToBST(self, nums: List[int]) -> TreeNode:
        def solve(nums):
            if nums:
                mid=len(nums)//2
                root=TreeNode(nums[mid])
                root.left=solve(nums[:mid])
                root.right=solve(nums[mid+1:])
                return root
        return solve(nums)
        