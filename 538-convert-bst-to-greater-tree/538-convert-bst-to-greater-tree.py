# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def convertBST(self, root: Optional[TreeNode]) -> Optional[TreeNode]:
        prev=0
        def solve(root):
            nonlocal prev
            if root==None:
                return prev
            solve(root.right)
            root.val+=prev
            # print(root.val)
            prev=root.val
            solve(root.left)
        solve(root)
        return root