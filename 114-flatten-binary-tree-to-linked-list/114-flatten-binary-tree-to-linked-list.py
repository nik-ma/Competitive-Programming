# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def flatten(self, root: Optional[TreeNode]) -> None:
        """
        Do not return anything, modify root in-place instead.
        
        
        """
        if root==None:
            return 
        pre=[]
        def preorder(root):
            if root==None:
                return
            pre.append(root)
            preorder(root.left)
            preorder(root.right)
        preorder(root)
        root.left=None
        head=root
        for i in range(1,len(pre)):
            pre[i].left=None
            head.right=pre[i]
            head=pre[i]
        root=head
            
            