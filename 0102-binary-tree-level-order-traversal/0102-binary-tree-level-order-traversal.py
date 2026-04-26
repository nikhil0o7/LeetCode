# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def levelOrder(self, root: Optional[TreeNode]) -> List[List[int]]:
        if not root:
            return []
        ans = []
        queue = deque([root])
        while queue:
            n = len(queue)
            curr_level = []
            for i in range(n):
                curr = queue.popleft()

                if curr.left:
                    queue.append(curr.left)

                if curr.right:
                    queue.append(curr.right)

                curr_level.append(curr.val)

            ans.append(curr_level)

        return ans