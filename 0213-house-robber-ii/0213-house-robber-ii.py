class Solution:
    def rob(self, nums: List[int]) -> int:
        memo = {}
        n = len(nums)
        if n == 1:
            return nums[0]
        def helper(i, nums, memo):
            if i >= len(nums):
                return 0

            if i in memo:
                return memo[i]

            ans = max(helper(i + 1, nums, memo), helper(i + 2, nums, memo) + nums[i])

            memo[i] = ans

            return ans
        return max(helper(0, nums[:-1], {}), helper(0, nums[1:], {}))
        