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
                cols[c].add(board[r][c])

                if board[r][c] in rows[r]:
                    return False
                rows[r].add(board[r][c])

                curr_r = r // 3
                curr_c = c // 3
                if board[r][c] in squares[(curr_r,curr_c)]:
                    return False

                squares[(curr_r, curr_c)].add(board[r][c])

        return True
        