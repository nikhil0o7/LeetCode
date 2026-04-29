class Solution:
    def rob(self, nums: List[int]) -> int:
        if len(nums) == 1:
            return nums[0]
        def helper(inp) -> int:
            n = len(inp)
            dp = [-1] * n
            dp[0] = inp[0]
            if len(inp) == 1:
                return dp[0]
            dp[1] = max(dp[0],inp[1])
            for i in range(2, n):
                dp[i] = max(dp[i - 1], inp[i] + dp[i - 2])
            return dp[-1]

        return max(helper(nums[1:]), helper(nums[:-1]))
        