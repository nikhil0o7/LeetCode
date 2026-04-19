class Solution:
    def maxAreaOfIsland(self, grid: List[List[int]]) -> int:
        ans = 0
        seen = set()
        ROWS = len(grid)
        COLS = len(grid[0])
        directions = [(0,1),(0,-1),(1,0),(-1,0)]

        def valid_cell(r,c) -> bool:
            return 0 <= r < ROWS and 0 <= c < COLS and grid[r][c] == 1

        for r in range(ROWS):
            for c in range(COLS):
                if (r,c) not in seen and grid[r][c] == 1:
                    seen.add((r,c))
                    shape = 0
                    stack = [(r,c)]
                    while stack:
                        row,col = stack.pop()
                        shape +=1
                        for dx,dy in directions:
                            curr_r, curr_c = row + dx, col + dy
                            if valid_cell(curr_r,curr_c) and (curr_r,curr_c) not in seen:
                                seen.add((curr_r,curr_c))
                                stack.append((curr_r,curr_c))
                    ans = max(shape,ans)


        return ans

        