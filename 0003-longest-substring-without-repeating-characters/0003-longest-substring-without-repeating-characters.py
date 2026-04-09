class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        l = r = 0
        chars = Counter()
        ans = 0

        while r < len(s):
            right = s[r]
            chars[right] += 1
            while chars[right] > 1:
                left = s[l]
                chars[left] -= 1
                l +=1
            ans = max(ans, r - l + 1)
            r += 1

        return ans