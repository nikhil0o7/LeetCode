class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        l,r = 0, 0
        ans = 0
        maxf = 0
        freq = Counter()

        for r in range(len(s)):
            right = s[r]
            freq[right] += 1
            maxf = max(maxf, freq[right])
            if (r - l + 1) - maxf > k:
                left = s[l]
                freq[left] -= 1
                l += 1
            ans = max(ans, r - l + 1)
        return ans