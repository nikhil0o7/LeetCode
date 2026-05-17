from typing import List

class DSU:
    def __init__(self, n):
        self.root = list(range(n))
        self.rank = [0] * n

    def find(self, node):
        if self.root[node] != node:
            self.root[node] = self.find(self.root[node])
        return self.root[node]

    def union(self, u, v):
        pu = self.find(u)
        pv = self.find(v)

        if pu == pv:
            return False

        if self.rank[pu] < self.rank[pv]:
            self.root[pu] = pv
        elif self.rank[pu] > self.rank[pv]:
            self.root[pv] = pu
        else:
            self.root[pv] = pu
            self.rank[pu] += 1

        return True


class Solution:
    def numIslands2(self, m: int, n: int, positions: List[List[int]]) -> List[int]:
        dsu = DSU(m * n)
        grid = [[0] * n for _ in range(m)]

        ans = []
        islands = 0

        directions = [(1, 0), (-1, 0), (0, 1), (0, -1)]

        for new_r, new_c in positions:
            if grid[new_r][new_c] == 1:
                ans.append(islands)
                continue

            grid[new_r][new_c] = 1
            islands += 1

            new_land = n * new_r + new_c

            for dr, dc in directions:
                old_r = new_r + dr
                old_c = new_c + dc

                if 0 <= old_r < m and 0 <= old_c < n and grid[old_r][old_c] == 1:
                    old_land = n * old_r + old_c

                    if dsu.union(new_land, old_land):
                        islands -= 1

            ans.append(islands)

        return ans