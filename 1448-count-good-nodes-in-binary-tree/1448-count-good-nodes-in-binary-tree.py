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
        count = 0
        def dfs(node, maxVal) -> None:
            if not node:
                return
            nonlocal count
            if node.val >= maxVal:
                count += 1
                maxVal = node.val

            left = dfs(node.left, maxVal)
            right = dfs(node.right, maxVal)
        dfs(root, root.val)
        return count

