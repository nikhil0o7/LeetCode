class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        left = right =0
        chars = Counter()
        ans = 0

        while right < len(s):
            r = s[right]
            chars[r] += 1
            while chars[r] > 1:
                l = s[left]
                chars[l] -= 1
                left +=1

            ans = max(ans, right - left + 1)
            right += 1
        return ans



        