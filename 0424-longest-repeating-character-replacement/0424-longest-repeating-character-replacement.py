class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        freq = Counter()
        maxf = 0
        ans = 0
        l,r = 0,0
        while r < len(s):
            right = s[r]
            freq[right] += 1
            maxf = max(maxf, freq[right])
            if (r - l + 1) - maxf > k:
                left = s[l]
                freq[left] -= 1
                l += 1
            ans = max(ans, r - l + 1)
            r += 1

        return ans

        