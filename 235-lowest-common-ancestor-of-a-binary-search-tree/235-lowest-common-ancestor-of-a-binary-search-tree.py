# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def lowestCommonAncestor(self, root: 'TreeNode', p: 'TreeNode', q: 'TreeNode') -> 'TreeNode':
        def find(root,p,q):
            if root==None:
                return 
            if root.val>=min(p.val,q.val) and root.val<=max(q.val,p.val):
                return root
            if root.val<min(p.val,q.val):
                return find(root.right,p,q)
            return find(root.left,p,q)
        return find(root,p,q)
        