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
        queue = deque([root])

        ans = []
        while queue:

            size = len(queue)
            curr_level = []

            for i in range(size):
                curr = queue.popleft()

                curr_level.append(curr.val)
                if curr.left:
                    queue.append(curr.left)

                if curr.right:
                    queue.append(curr.right)

            ans.append(curr_level)

        return ans
        