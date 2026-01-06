class Solution:
    def longestPalindrome(self, s: str) -> str:
        n = len(s)
        # create a table of size n
        dp= [[False] * n for _ in range(n)]
        ans = [0,0]
        #all the one word's are definitely a palindrome
        for i in range(n):
            dp[i][i] = True

        #if two words are same then they're a palindrome as well
        for i in range(n - 1):
            if s[i] == s[i+1]:
                dp[i][i+1] = True
                ans = [i,i+1]

        for diff in range(2,n):
            for i in range(n - diff):
                j = i + diff
                #if two characters are equal and the previous ones are true, then its a palindrome
                if s[i] == s[j] and dp[i + 1][j-1]:
                    dp[i][j] = True  
                    ans = [i,j]

        i,j = ans
        return s[i : j +1]      