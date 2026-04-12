class Solution:
    def runningSum(self, nums: List[int]) -> List[int]:
        currSum = 0
        for i,num in enumerate(nums):
            temp = num + currSum
            currSum += num
            nums[i] = temp
        return nums
        