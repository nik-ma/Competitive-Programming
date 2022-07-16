# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def buildTree(self, inorder: List[int], postorder: List[int]) -> Optional[TreeNode]:
        def solve(inorder,postorder):
            if inorder and postorder:
                val=postorder.pop()
                root=TreeNode(val)
                ind=inorder.index(val)
                root.right=solve(inorder[ind+1:],postorder)
                root.left=solve(inorder[:ind],postorder)
                return root
        return solve(inorder,postorder)
                
        
        