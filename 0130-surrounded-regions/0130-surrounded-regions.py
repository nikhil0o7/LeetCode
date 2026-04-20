class Solution:
    def solve(self, board: List[List[str]]) -> None:
        """
        Do not return anything, modify board in-place instead.
        """
        ROWS = len(board)
        COLS = len(board[0])
        queue = deque()
        
        for r in range(ROWS):
            for c in range(COLS):
                if (r == 0 or r == ROWS - 1 or c == 0 or c == COLS - 1) and board[r][c] == "O":
                    queue.append((r,c))

        directions = [(0,1),(0,-1),(1,0),(-1,0)]
        while queue:
            for i in range(len(queue)):
                r,c = queue.popleft()
                if board[r][c] == "O":
                    board[r][c] = "T"
                    for dr,dc in directions:
                        row,col = r + dr, c + dc
                        if (0 <= row < ROWS and 0 <= col < COLS and board[r][c] == "O"):
                            queue.append((row,col))

        for r in range(ROWS):
            for c in range(COLS):
                if board[r][c] == "O":
                    board[r][c] = "X"
                elif board[r][c] == "T":
                    board[r][c] = "O"
            
        