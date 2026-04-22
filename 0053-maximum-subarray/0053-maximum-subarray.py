class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        ans = 0
        temp = 0
        for num in nums:
            temp += num
            ans = max(ans,temp)
            temp = 0 if temp < 0 else temp
        return ans
        