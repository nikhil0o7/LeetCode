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
        num_good_nodes = 0
        
        def dfs(node, val):
            if not node:
                return
            nonlocal num_good_nodes
            if node.val >= val:
                num_good_nodes += 1
                val = node.val
            dfs(node.left, val)
            dfs(node.right, val)

        dfs(root, root.val)
        return num_good_nodes 



        