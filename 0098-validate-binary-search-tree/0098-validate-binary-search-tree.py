# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def isValidBST(self, root: Optional[TreeNode]) -> bool:
        if not root:
            return True

        def dfs(node, leftVal, rightVal) -> bool:
            if not node:
                return True

            if leftVal >= node.val or rightVal <= node.val:
                return False
            
            left = dfs(node.left, leftVal, node.val)
            right = dfs(node.right, node.val, rightVal)

            return left and right

        return dfs(root,float("-inf"),float("inf"))