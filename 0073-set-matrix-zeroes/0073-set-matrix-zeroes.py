class Solution:
    def setZeroes(self, matrix: List[List[int]]) -> None:
        """
        Do not return anything, modify matrix in-place instead.
        """
        ROWS = len(matrix)
        COLS = len(matrix[0])
        rows = set()
        cols = set()

        for i in range(ROWS):
            for j in range(COLS):
                if matrix[i][j] == 0:
                    rows.add(i)
                    cols.add(j)

        for i in range(ROWS):
            for j in range(COLS):
                if i in rows or j in cols:
                    matrix[i][j] = 0
        