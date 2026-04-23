# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def zigzagLevelOrder(self, root: Optional[TreeNode]) -> List[List[int]]:
        if not root:
            return []

        queue = deque([root])
        ans = []
        level = 0
        while queue:
            n = len(queue)
            curr_stage = []
            for i in range(n):
                curr = queue.popleft()

                if curr.left:
                    queue.append(curr.left)

                if curr.right:
                    queue.append(curr.right)
                
                if level % 2 == 0:
                    curr_stage.append(curr.val)
                else:
                    curr_stage.insert(0, curr.val)
                    
            ans.append(curr_stage)
            level += 1

        return ans
        