class Solution:
    def getDirections(self, root: Optional[TreeNode], startValue: int, destValue: int) -> str:
            # 1) Create preorder DFS to find the lowest Common Ancestor:
            def dfsLCA(node):
                # Tree nodes exhausted:
                if not node:
                    return None

                # Node is descendant of itself:
                if node.val == startValue or node.val == destValue:
                    return node

                # Perform dfs preorder traversal:
                left_node = dfsLCA(node.left)
                right_node = dfsLCA(node.right)

                # LCA is found or continue looking:
                if left_node and right_node:
                    return node
                else:
                    return left_node or right_node


            # 2) Create backtracking method to create path/directions:
            def backtrack(node, path, val):
                # Destination has been reached
                if node.val == val:
                    return "".join(path)

                # Write/process path values at the left:
                if node.left:
                    path.append("L")
                    left = backtrack(node.left, path, val)
                    path.pop()
                    if left:
                        return left

                # Write/process path values at the right:
                if node.right:
                    path.append("R")
                    right = backtrack(node.right, path, val)
                    path.pop()
                    if right:
                        return right  

            # 3) DRIVE CODE:
            # a) Call LCA method to find lowest common ancestor of start and dest nodes:
            LCA = dfsLCA(root)

            # b) Create the path from each node (start/dest) to LCA:
            startPath = backtrack(LCA, [], startValue)
            destPath = backtrack(LCA, [], destValue)

            # c) Return the union of the 2 paths. But reverse the start path:
            return len(startPath) * "U" + destPath