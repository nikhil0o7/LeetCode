class Solution:
    def orangesRotting(self, grid: List[List[int]]) -> int:
        ROWS = len(grid)
        COLS = len(grid[0])
        fresh = 0
        time = 0
        queue = deque()
        for r in range(ROWS):
            for c in range(COLS):
                if grid[r][c] == 1:
                    fresh +=1
                elif grid[r][c] == 2:
                    queue.append((r,c))

        directions = [(0,1),(0,-1),(1,0),(-1,0)]
        while fresh > 0 and queue:
            for i in range(len(queue)):
                r,c = queue.popleft()
                for dx,dy in directions:
                    nr = r + dx
                    nc = c + dy

                    if 0 <= nr < ROWS and 0 <= nc < COLS and grid[nr][nc] == 1:
                        grid[nr][nc] = 2
                        fresh -= 1
                        queue.append((nr,nc))

            time +=1

        return time if fresh == 0 else -1