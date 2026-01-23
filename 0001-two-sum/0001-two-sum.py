class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        d = { }
        for i in range(len(nums)):
            compliment = target - nums[i]
            if compliment in d:
                return [d[compliment],i]
            d[nums[i]] = i

        return [-1,-1]
        