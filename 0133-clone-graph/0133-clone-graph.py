"""
# Definition for a Node.
class Node:
    def __init__(self, val = 0, neighbors = None):
        self.val = val
        self.neighbors = neighbors if neighbors is not None else []
"""

from typing import Optional
class Solution:
    def cloneGraph(self, node: Optional['Node']) -> Optional['Node']:
        if not node:
            return

        oldToNew = {}
        def dfs(root):
            if root in oldToNew:
                return oldToNew[root]

            copy = Node(root.val)
            oldToNew[root] = copy
            for neighbor in root.neighbors:
                copy.neighbors.append(dfs(neighbor))
            return copy

        return dfs(node)
        