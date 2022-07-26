# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def getDirections(self, root: Optional[TreeNode], startValue: int, destValue: int) -> str:
        def lca(root,p,q):
            if root==None or root.val==p or root.val==q:
                return root
            left=lca(root.left,p,q)
            right=lca(root.right,p,q)
            if left==None:
                return right
            if right==None:
                return left
            return root
        root=lca(root,startValue,destValue)
        def find(root,path,target):
            if root==None:
                return 
            if root.val==target:
                # ans.append(path)
                # lsfo
                return ''.join(path)
            path.append('L')
            left=find(root.left,path,target)
            if left:
                return left
            path.pop()
            path.append('R')
            right=find(root.right,path,target)
            if right:
                return right
            path.pop()
            return 
            
        ans=[]
        first=find(root,[],startValue)
        second=find(root,[],destValue)
        # print(second)
        return 'U'*(len(first))+''.join(second)
    
        