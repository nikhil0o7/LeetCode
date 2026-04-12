class Solution:
    def rob(self, nums: List[int]) -> int:
        memo = {}
        def helper(i, nums):
            if i >= len(nums):
                return 0
            nonlocal memo
            if i in memo:
                return memo[i]

            ans = max(helper(i + 1, nums), helper(i + 2, nums) + nums[i])

            memo[i] = ans

            return ans
        return helper(0, nums)