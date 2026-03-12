class Solution:
    def orangesRotting(self, grid: List[List[int]]) -> int:
        q = deque()
        time = 0
        fresh = 0
        ROWS, COLS = len(grid), len(grid[0])

        for r in range(ROWS):
            for c in range(COLS):
                if grid[r][c] == 1:
                    fresh += 1
                if grid[r][c] == 2:
                    q.append((r,c))

        directions = [(1,0),(-1,0),(0,1),(0,-1)]

        while fresh > 0 and q:
            length = len(q)
            for i in range(length):
                r, c = q.popleft()
                for dx,dy in directions:
                    curr_r, curr_c = r + dx, c + dy
                    if(curr_r in range(ROWS) and curr_c in range(COLS) and grid[curr_r][curr_c] == 1):
                        grid[curr_r][curr_c] = 2
                        q.append((curr_r,curr_c))
                        fresh -= 1
                        
            time +=1

        return time if fresh == 0 else - 1     