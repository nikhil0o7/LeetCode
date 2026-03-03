class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        #kadane's algorithm
        # if we have get a -ve sum by adding the current element we don't take that one
        temp = 0
        maxi = float("-inf")

        for i in nums:
            temp += i
            maxi = max(maxi,temp)
            temp = 0 if temp < 0 else temp

        return maxi