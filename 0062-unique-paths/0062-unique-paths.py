class Solution:
    def uniquePaths(self, m: int, n: int) -> int:
        memo = [[-1] * (n + 1) for _ in range(m + 1)]
        def dfs(i,j):
            if i == m - 1 and j == n - 1:
                return 1
            if i >= m or j >= n:
                return 0
            if memo[i][j]!= -1:
                return memo[i][j]

            right = dfs(i, j + 1)
            down = dfs(i + 1, j)
            memo[i][j] = right + down

            return memo[i][j]
        return dfs(0,0)
        