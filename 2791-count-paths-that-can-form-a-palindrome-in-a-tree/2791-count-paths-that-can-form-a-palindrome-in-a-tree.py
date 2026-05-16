from typing import List
from collections import defaultdict

class Solution:
    def countPalindromePaths(self, parent: List[int], s: str) -> int:
        n = len(parent)

        graph = defaultdict(list)

        for child in range(1, n):
            graph[parent[child]].append(child)

        count = defaultdict(int)
        count[0] = 1

        ans = 0

        def dfs(node, mask):
            nonlocal ans

            for child in graph[node]:
                char_index = ord(s[child]) - ord('a')
                child_mask = mask ^ (1 << char_index)
                # print(child_mask)
                # print(count)/
                # Case 1: same mask
                ans += count[child_mask]
                
                # Case 2: differs by exactly one character
                for i in range(26):
                    ans += count[child_mask ^ (1 << i)]

                # Store this node's root-to-node mask
                count[child_mask] += 1
                print(child,child_mask)
                dfs(child, child_mask)

        dfs(0, 0)
        return ans