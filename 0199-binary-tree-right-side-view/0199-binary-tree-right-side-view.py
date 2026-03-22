# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def rightSideView(self, root: Optional[TreeNode]) -> List[int]:
        if not root:
            return []
        queue = deque([root])
        ans = []

        while queue:
            size = len(queue)

            for i in range(size):
                curr = queue.popleft()

                if curr.left:
                    queue.append(curr.left)

                if curr.right:
                    queue.append(curr.right)
                    
                if i + 1 == size:
                    ans.append(curr.val)

        return ans
        