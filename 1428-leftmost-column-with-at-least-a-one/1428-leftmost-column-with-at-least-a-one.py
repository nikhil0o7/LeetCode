# """
# This is BinaryMatrix's API interface.
# You should not implement it, or speculate about its implementation
# """
#class BinaryMatrix(object):
#    def get(self, row: int, col: int) -> int:
#    def dimensions(self) -> list[]:

class Solution:
    def leftMostColumnWithOne(self, binaryMatrix: 'BinaryMatrix') -> int:
        rows, cols = binaryMatrix.dimensions()
        smallest_index = cols
        for row in range(rows):
            low = 0
            high = cols  - 1
            while low < high:
                mid = (low + high) // 2
                if binaryMatrix.get(row,mid) == 0:
                    low = mid + 1
                else:
                    high = mid

            if binaryMatrix.get(row,low) == 1:
                smallest_index = min(smallest_index, low)

        return -1 if smallest_index == cols else smallest_index

        