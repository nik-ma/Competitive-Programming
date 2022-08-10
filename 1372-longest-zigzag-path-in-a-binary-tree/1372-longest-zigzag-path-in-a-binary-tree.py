# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def longestZigZag(self, root: Optional[TreeNode]) -> int:
        if root==None:
            return 0
        maxi=0
        def solve(root,count,flag):
            nonlocal maxi
            if root==None:
                return 
            maxi=max(maxi,count)
            if flag=='right':
                if root.left:
                    solve(root.left,count+1,'left')
                if root.right:
                    solve(root.right,1,'right')
            elif flag=='left':
                if root.right:
                    solve(root.right,count+1,'right')
                if root.left:
                    solve(root.left,1,'left')
        solve(root.right,1,'right')
        solve(root.left,1,'left')
        return maxi
                
                    
            
            