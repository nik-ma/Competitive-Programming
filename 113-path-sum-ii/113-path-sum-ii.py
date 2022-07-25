# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def pathSum(self, root: Optional[TreeNode], targetSum: int) -> List[List[int]]:
        ans=[]
        def solve(root,targetSum,res):
            # if targetSum<0:
            #     return 
            if root==None:
                return 
            if root.left==None and root.right==None:
                if root.val==targetSum:
                    res.append(root.val)
                    ans.append(res[:])
                    res.pop()
            res.append(root.val)
            if root.right:
                solve(root.right,targetSum-root.val,res)
            if root.left:
                solve(root.left,targetSum-root.val,res)
            res.pop()
            return 
        solve(root,targetSum,[])
        return ans
                    