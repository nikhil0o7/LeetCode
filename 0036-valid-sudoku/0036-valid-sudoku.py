class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        ROWS = len(board)
        COLS = len(board[0])

        rowset = defaultdict(set)
        colset = defaultdict(set)
        boxset = defaultdict(set)

        for r in range(ROWS):
            for c in range(COLS):
                if board[r][c] == ".":
                    continue

                if board[r][c] in rowset[r]:
                    return False
                rowset[r].add(board[r][c])

                if (r,c) in colset[c]:
                    return False
                colset[c].add(board[r][c])

                box = (r // 3, c // 3)
                if board[r][c] in boxset[box]:
                    return False
                boxset[box].add(board[r][c])


        return True
        