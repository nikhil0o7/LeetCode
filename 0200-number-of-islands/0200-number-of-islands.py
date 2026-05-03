class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        ROWS = len(grid)
        COLS = len(grid[0])
        ans = 0
        seen = set()
        directions = [(0,1),(0,-1),(1,0),(-1,0)]

        def valid_cell(r,c):
            return 0 <= r < ROWS and 0 <= c < COLS and (r,c) not in seen and grid[r][c] == "1"

        def dfs(r,c):
            for dx,dy in directions:
                curr_r,curr_c = dx + r, dy + c
                if valid_cell(curr_r,curr_c):
                    seen.add((curr_r,curr_c))
                    dfs(curr_r,curr_c)

        for r in range(ROWS):
            for c in range(COLS):
                if grid[r][c] == "1" and (r,c) not in seen:
                    seen.add((r,c))
                    ans += 1
                    dfs(r,c)

        return ans





