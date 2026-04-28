class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        ROWS = len(matrix)
        COLS = len(matrix[0])
        top = 0
        bot = ROWS - 1
        while top <= bot:
            mid = (top + bot) // 2
            if matrix[mid][0] > target:
                bot = mid - 1
            elif matrix[mid][-1] < target:
                top = mid + 1
            else:
                break

        if not top <= bot:
            return False
       
        row = (top + bot) //2
        l,r = 0, COLS - 1
        while l <= r:
            mid = (l + r) // 2
            if matrix[row][mid] == target:
                return True
            elif matrix[row][mid] > target:
                r = mid - 1
            elif matrix[row][mid] < target:
                l = mid + 1
        return False        
        