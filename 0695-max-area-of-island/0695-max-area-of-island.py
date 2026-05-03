class Solution:
    def maxAreaOfIsland(self, grid: List[List[int]]) -> int:
        ans = 0
        ROWS = len(grid)
        COLS = len(grid[0])
        seen = set()
        directions = [(0,1),(0,-1),(1,0),(-1,0)]

        def valid_cell(dr,dc):
            return 0 <= dr < ROWS and 0 <= dc < COLS and grid[dr][dc] == 1


        for r in range(ROWS):
            for c in range(COLS):
                curr = 0
                if grid[r][c] == 1 and (r,c) not in seen:
                    seen.add((r,c))
                    stack = []
                    curr += 1
                    stack.append((r,c))
                    while stack:
                        curr_r,curr_c = stack.pop()
                        for dx,dy in directions:
                            dr,dc = dx + curr_r ,dy + curr_c
                            if valid_cell(dr,dc) and (dr,dc) not in seen :
                                curr += 1
                                seen.add((dr,dc))
                                stack.append((dr,dc))
                            
                    ans = max(ans, curr)


        return ans