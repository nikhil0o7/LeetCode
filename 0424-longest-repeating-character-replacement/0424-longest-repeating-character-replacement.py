class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        ans , l = 0, 0 
        maxf = 0
        freq = {}

        for r in range(len(s)):
            freq[s[r]] = 1 + freq.get(s[r],0)
            maxf = max(maxf, freq[s[r]])
            if (r - l + 1) - maxf > k:
                freq[s[l]] -= 1
                l += 1

            ans = max(ans, r - l + 1)
        return ans
        