class Solution:
    def pacificAtlantic(self, heights: List[List[int]]) -> List[List[int]]:
        ROWS , COLS = len(heights), len(heights[0])
        pac = [[False] * COLS for _ in range(ROWS)]
        atl = [[False] * COLS for _ in range(ROWS)]
        directions = [(1,0),(-1,0),(0,1),(0,-1)]
        pacific = []
        atlantic = []

        def bfs(source,ocean):
            q = deque(source)
            while q:
                r,c = q.popleft()
                ocean[r][c] = True
                for dx,dy in directions:
                    row,col = r + dx, c + dy

                    if (0 <= row < ROWS and 0 <= col < COLS and not ocean[row][col] and heights[row][col] >= heights[r][c]):
                        q.append((row,col))

        for c in range(COLS):
            pacific.append((0,c))
            atlantic.append((ROWS-1,c))
        
        for r in range(ROWS):
            pacific.append((r,0))
            atlantic.append((r,COLS - 1))

        bfs(pacific, pac)
        bfs(atlantic, atl)

        res = []

        for r in range(ROWS):
            for c in range(COLS):
                if pac[r][c] and atl[r][c]:
                    res.append([r,c])

        return res
        