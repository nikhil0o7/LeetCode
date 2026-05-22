class Solution:
    def longestPalindrome(self, s: str) -> str:
        if len(s) == 1:
            return s
        n = len(s)
        dp = [[False] * len(s) for _ in range(n)]
        for i in range(len(s)):
            dp[i][i] = True
        ans = [0,0]
        for i in range(n - 1):
            if s[i] == s[i + 1]:
                dp[i][i + 1] = True
                ans = [i, i + 1]

        for diff in range(2,n):
            for i in range(n - diff):
                j = i + diff
                if s[i] == s[j] and dp[i + 1][j - 1]:
                    dp[i][j] = True
                    ans = [i,j]


        x,y = ans
        return s[x : y + 1]
        

        