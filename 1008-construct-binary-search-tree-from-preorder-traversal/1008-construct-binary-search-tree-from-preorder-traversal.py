# class TreeNode:
#     def __init__(self, val, left = None, right = None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def bstFromPreorder(self, preorder: List[int]) -> Optional[TreeNode]:
        n = len(preorder)
        idx = 0
        def dfs(lower, upper) -> Optional[TreeNode]:
            nonlocal idx
            if idx == n:
                return None

            val = preorder[idx]
            
            if val < lower or val > upper:
                return None

            idx += 1
            root = TreeNode(val)
            root.left = dfs(lower,val)
            root.right = dfs(val, upper)
            return root


        return dfs(float("-inf"), float("inf"))









        