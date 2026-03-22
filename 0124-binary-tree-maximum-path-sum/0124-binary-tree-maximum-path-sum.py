# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def maxPathSum(self, root: Optional[TreeNode]) -> int:
        ans = root.val
        def dfs(node) -> int:
            if not node:
                return 0
            nonlocal ans
            leftMax = dfs(node.left)
            rightMax = dfs(node.right)
            left = max(leftMax, 0)
            right = max(rightMax, 0)
            ans = max(ans, node.val + left + right)
            return node.val + max(left,right)

        dfs(root)
        return ans




        