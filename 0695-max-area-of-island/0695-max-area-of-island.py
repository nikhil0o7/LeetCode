class Solution:
    def maxAreaOfIsland(self, grid: List[List[int]]) -> int:
        ROWS = len(grid)
        COLS = len(grid[0])
        area = 0
        directions = [(0,1),(0,-1),(1,0),(-1,0)]
        seen = set()

        def valid_cell(r,c):
            return 0 <= r < ROWS and 0 <= c < COLS and grid[r][c] == 1
        for r in range(ROWS):
            for c in range(COLS):
                if grid[r][c]==1:
                    stack = []
                    stack.append((r,c))
                    seen.add((r,c))
                    shape = 0
                    while stack:
                        r,c = stack.pop()
                        shape +=1
                        for dx,dy in directions:
                            curr_r = r + dx
                            curr_c = c + dy
                            if valid_cell(curr_r,curr_c) and (curr_r,curr_c) not in seen:
                                seen.add((curr_r,curr_c))
                                stack.append((curr_r,curr_c))

                    area = max(shape,area)

        return area

        