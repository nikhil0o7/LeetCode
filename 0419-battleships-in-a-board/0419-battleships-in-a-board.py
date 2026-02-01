class Solution:
    def countBattleships(self, board: List[List[str]]) -> int:
        M = len(board)
        N = len(board[0])

        count = 0
        for row in range(M):
            for col in range(N):
                if board[row][col] == 'X':
                    isLeftMost = col - 1 != -1 and board[row][col - 1] == 'X'
                    isTopMost = row - 1 != -1 and board[row - 1][col] == 'X'
                    if not isLeftMost and not isTopMost:
                        count += 1
        return count
        