# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def maxProduct(self, root: Optional[TreeNode]) -> int:
        allSums = []
        
        def treeSum(subRoot):
            if subRoot is None: return 0
            left = treeSum(subRoot.left)
            right = treeSum(subRoot.right)
            totalSum = subRoot.val + left + right
            allSums.append(totalSum)
            return totalSum

        total = treeSum(root)
        best = 0
        for s in allSums:
            best = max(best, s * (total - s))

        return best % (10 ** 9 + 7)

        