# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def diameterOfBinaryTree(self, root: Optional[TreeNode]) -> int:
        ans=[0]
        def diameter(root):
            if root==None:
                return 0
            right=diameter(root.right)
            left=diameter(root.left)
            ans[0]=max(ans[0],right+left)
            return 1+max(right,left)
        diameter(root)
        return ans[0]
        