class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        s = set(nums)
        best = 0

        for x in s:  # iterate unique values (avoids duplicate work)
            if x - 1 not in s:          # start of a sequence
                y = x
                while y in s:
                    y += 1
                best = max(best, y - x) # length

        return best



