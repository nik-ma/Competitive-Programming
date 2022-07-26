# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def lowestCommonAncestor(self, root: 'TreeNode', p: 'TreeNode', q: 'TreeNode') -> 'TreeNode':
        if root==None or root==p or root==q:
            return root
        lef=self.lowestCommonAncestor(root.left,p,q)
        righ=self.lowestCommonAncestor(root.right,p,q)
        if lef==None:
            return righ
        if righ==None:
            return lef
        return root
        