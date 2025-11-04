class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        d = {}
        for i in range(len(nums)):
            tar = target - nums[i]
            if tar in d:
                return [i, d[tar]]
            d[nums[i]] = i

        return [-1,-1]
