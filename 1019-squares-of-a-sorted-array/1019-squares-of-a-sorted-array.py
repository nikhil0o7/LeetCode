class Solution:
    def sortedSquares(self, nums: List[int]) -> List[int]:
        result = [0] * len(nums)
        left, right = 0 , len(nums) - 1
        for i in range(len(nums) - 1, -1 , -1):
            if abs(nums[left]) > abs(nums[right]):
                sq = nums[left]
                left +=1
            else:
                sq = nums[right]
                right -=1
            result[i] = sq * sq
        return result

