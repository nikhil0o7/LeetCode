class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        ROWS = len(board)
        COLS = len(board[0])
        rows = defaultdict(set)
        cols = defaultdict(set)
        squares = defaultdict(set)

        for r in range(ROWS):
            for c in range(COLS):
                if board[r][c] == ".":
                    continue

                if board[r][c] in cols[c]:
                    return False
                cols[c].append(board[r][c])


                if board[r][c] in rows[r]:
                    return False
                rows[r].append(board[r][c])

                box = board[r][c] // 3


        return True
        