class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        countS = defaultdict(int)
        l = r = 0
        ans = 0
        while r < len(s):
            countS[s[r]] += 1
            # print(countS)
            while countS[s[r]] > 1:
                left = s[l]
                countS[left] -= 1
                l+= 1
            ans = max(ans, r - l + 1)
            r+=1

        return ans

        