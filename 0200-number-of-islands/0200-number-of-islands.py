class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        ROWS = len(grid)
        COLS = len(grid[0])
        seen = set()
        directions = [(0,1),(0,-1),(1,0),(-1,0)]
        ans = 0

        def valid_cell(r,c) -> bool:
            return 0 <= r < ROWS and 0 <= c < COLS and grid[r][c] == "1"

        for r in range(ROWS):
            for c in range(COLS):
                if grid[r][c] == "1" and (r,c) not in seen:
                    stack = []
                    stack.append((r,c))
                    seen.add((r,c))
                    ans+=1
                    while stack:
                        row,col = stack.pop()
                        for dx,dy in directions:
                            curr_r,curr_c= dx + row, dy + col
                            if valid_cell(curr_r,curr_c) and (curr_r,curr_c) not in seen:
                                seen.add((curr_r,curr_c))
                                stack.append((curr_r,curr_c))
        return ans        