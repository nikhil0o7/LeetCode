class Solution:
    def maxAreaOfIsland(self, grid: List[List[int]]) -> int:
        ROWS = len(grid)
        COLS = len(grid[0])
        area = 0
        seen = set()

        def dfs(r,c) -> int:
            if (0 > r or r == ROWS or 0 > c or c == COLS or (r,c) in seen or grid[r][c] == 0):
                return 0
           
            seen.add((r,c))
            return (1 +  dfs(r + 1,c) + dfs(r - 1, c) + dfs(r, c + 1) + dfs(r, c- 1))


        for r in range(ROWS):
            for c in range(COLS):
                area = max(area, dfs(r,c))


        return area
        