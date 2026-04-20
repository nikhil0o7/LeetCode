class Solution:
    def pacificAtlantic(self, heights: List[List[int]]) -> List[List[int]]:
        ROWS = len(heights)
        COLS = len(heights[0])
        pac = [[False] * COLS for _ in range(ROWS)]
        atl = [[False] * COLS for _ in range(ROWS)]
        # print(pac,atl)
        pacific = []
        atlantic = []
        directions = [(0,1),(0,-1),(1,0),(-1,0)]

        def bfs(source,ocean):
            queue = deque(source)
            while queue:
                r,c = queue.popleft()
                ocean[r][c] = True
                for dx,dy in directions:
                    row = r + dx
                    col = c + dy
                    if (0 <= row < ROWS and 0 <= col < COLS and not ocean[row][col] and heights[row][col] >= heights[r][c]):
                        queue.append((row,col))



        for r in range(ROWS):
            pacific.append((r,0))
            atlantic.append((r,COLS - 1))
        
        for c in range(COLS):
            pacific.append((0,c))
            atlantic.append((ROWS - 1, c))

        bfs(pacific,pac)
        bfs(atlantic,atl)
        res = []
        for r in range(ROWS):
            for c in range(COLS):
                if pac[r][c] and atl[r][c]:
                    res.append([r,c])


        return res