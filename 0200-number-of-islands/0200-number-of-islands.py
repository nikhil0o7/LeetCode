class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        if not grid or not grid[0]:
            return 0

        ROWS = len(grid)
        COLS = len(grid[0])
        seen = set()
        directions = [(0,1), (0,-1), (1,0), (-1,0)]
        ans = 0

        def valid_cell(r, c) -> bool:
            return 0 <= r < ROWS and 0 <= c < COLS and grid[r][c] == "1"

        for r in range(ROWS):
            for c in range(COLS):
                if grid[r][c] == "1" and (r, c) not in seen:
                    ans += 1
                    seen.add((r, c))
                    stack = [(r, c)]

                    while stack:
                        row, col = stack.pop()

                        for dx, dy in directions:
                            curr_r = row + dx
                            curr_c = col + dy

                            if valid_cell(curr_r, curr_c) and (curr_r, curr_c) not in seen:
                                seen.add((curr_r, curr_c))
                                stack.append((curr_r, curr_c))

        return ans