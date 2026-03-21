# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def maxDepth(self, root: Optional[TreeNode]) -> int:
        if not root:
            return 0

        def dfs(node, depth) -> int:
            if not node:
                return 0

            left = dfs(node.left, depth)
            right = dfs(node.right, depth)
            
            depth = 1 + max(left, right)

            return depth

        return dfs(root, 0)
        