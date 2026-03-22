# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def goodNodes(self, root: TreeNode) -> int:
        if not root:
            return 0
        ans = 0

        def dfs(node, max_val):
            if not node:
                return
            nonlocal ans
            if node.val >= max_val:
                ans += 1
                max_val = node.val

            dfs(node.left, max_val)
            dfs(node.right, max_val)

        dfs(root, root.val)
        return ans
        