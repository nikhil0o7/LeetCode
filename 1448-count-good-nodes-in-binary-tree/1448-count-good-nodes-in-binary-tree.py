# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def goodNodes(self, root: TreeNode) -> int:
        maxVal = root.val
        ans = 0
        def dfs(node) -> None:
            if not node:
                return
            nonlocal ans,maxVal
            if node.val >= maxVal:
                ans += 1
                maxVal = node.val
            dfs(node.left)
            dfs(node.right)

        dfs(root)
        return ans
        