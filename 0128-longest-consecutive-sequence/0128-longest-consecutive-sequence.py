class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        s = set(nums)
        ans = 0

        for num in s:
            if num - 1 not in s:
                y = num 
                while y in s:
                    y += 1
                    ans = max(ans, y - num)

        return ans

