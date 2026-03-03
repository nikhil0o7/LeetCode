# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def isValidBST(self, root):
        prev = None
        cur = root

        while cur:
            if cur.left is None:
                if prev is not None and cur.val <= prev:
                    return False
                prev = cur.val
                cur = cur.right
            else:
                pre = cur.left
                while pre.right and pre.right is not cur:
                    pre = pre.right

                if pre.right is None:
                    pre.right = cur
                    cur = cur.left
                else:
                    pre.right = None
                    if prev is not None and cur.val <= prev:
                        return False
                    prev = cur.val
                    cur = cur.right

        return True