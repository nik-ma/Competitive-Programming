# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
from collections import Counter
class Solution:
    def pathSum(self, root: Optional[TreeNode], targetSum: int) -> int:
        dicti=Counter()
        # res=0
        dicti[0]=1
        target=targetSum
        def solve(root,curr):
            # nonlocal res
            if root==None:
                return 0
            curr+=root.val
            res=0
            if curr-target in dicti:
                res+= dicti[curr-target]
            dicti[curr]+=1
            res+=solve(root.left,curr)
            res+=solve(root.right,curr)
            dicti[curr]-=1
            return res
        return solve(root,0)