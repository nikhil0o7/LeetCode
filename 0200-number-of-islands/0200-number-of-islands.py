class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        ROWS = len(grid)
        COLS = len(grid[0])
        ans = 0
        seen = set()
        directions = [(1,0),(-1,0),(0,-1),(0,1)]

        def valid_cell(r,c):
            return 0 <= r < ROWS and 0 <= c < COLS and grid[r][c] == "1"

        def dfs(r,c):
            for dx,dy in directions:
                next_dx, next_dy = r + dx, c + dy
                if valid_cell(next_dx, next_dy) and (next_dx,next_dy) not in seen:
                    seen.add((next_dx,next_dy))
                    dfs(next_dx,next_dy)

        for row in range(ROWS):
            for col in range(COLS):
                if grid[row][col] == "1" and (row,col) not in seen:
                    ans += 1
                    seen.add((row,col))
                    dfs(row,col)

        return ans
