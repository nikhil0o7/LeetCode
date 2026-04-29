class Solution:
    def solveNQueens(self, n: int) -> List[List[str]]:
        posDig = set()
        negDig = set()
        col = set()
        res = []
        board = [["."] * n for _ in range(n)]
        def backtrack(r):
            if r == n:
                copy = ["".join(row) for row in board]
                res.append(copy)
                return
            for c in range(n):
                if (r + c) in posDig or c in col or (r - c) in negDig:
                    continue
                posDig.add(r + c)
                negDig.add(r - c)
                col.add(c)
                board[r][c] = "Q"
                backtrack(r + 1)
                posDig.remove(r + c)
                negDig.remove(r - c)
                col.remove(c)
                board[r][c] = "."
        backtrack(0)

        return res

        