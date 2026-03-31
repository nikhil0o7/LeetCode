class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        ROWS = len(grid)
        COLS = len(grid[0])
        seen = set()
        ans = 0
        directions = [(1,0),(-1,0),(0,1),(0,-1)]
        
        def valid_cell(r,c) -> bool:
            return 0 <= r < ROWS and 0 <= c < COLS and grid[r][c] == "1"

        def dfs(x,y) -> None:
            for dx,dy in directions:
                curr_r,curr_c = dx+x, dy + y
                if valid_cell(curr_r,curr_c) and (curr_r,curr_c) not in seen:
                    seen.add((curr_r,curr_c))
                    dfs(curr_r,curr_c)

        for r in range(ROWS):
            for c in range(COLS):
                if grid[r][c] == "1" and (r,c) not in seen:
                    ans +=1
                    seen.add((r,c))
                    dfs(r,c)

        return ans
        