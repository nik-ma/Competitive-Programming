# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def isValidBST(self, root: TreeNode) -> bool:
        rang=[-float('inf'),float('inf')]
        def helper(root,rang):
            if root==None:
                return True
            if rang[0]<root.val<rang[1]:
                return helper(root.right,[root.val,rang[1]]) and helper(root.left,[rang[0],root.val])  
            else:
                return False
            
        return helper(root,rang)
            
        
                
                
        