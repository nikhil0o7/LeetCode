class Solution:
    def orangesRotting(self, grid: List[List[int]]) -> int:
        queue = deque()
        fresh = 0
        time = 0
        ROWS, COLS = len(grid), len(grid[0])

        for r in range(ROWS):
            for c in range(COLS):
                if grid[r][c] == 1:
                    fresh += 1
                elif grid[r][c] == 2:
                    queue.append((r,c))

        directions = [(1,0),(-1,0),(0,1),(0,-1)]

        while fresh > 0 and queue:
            for i in range(len(queue)):
                r,c = queue.popleft()
                for dx,dy in directions:
                    curr_r, curr_c = dx + r, dy + c
                    if (0 <= curr_r < ROWS and 0 <= curr_c < COLS and grid[curr_r][curr_c] == 1):
                        grid[curr_r][curr_c] = 2
                        fresh -= 1
                        queue.append((curr_r,curr_c))
            time +=1
        print(fresh,time)
        return time if fresh == 0 else - 1
        