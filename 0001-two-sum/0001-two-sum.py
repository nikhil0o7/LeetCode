class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        d = {}
        for i in range(len(nums)):
            compl = target  - nums[i]
            if compl in d:
                return [d[compl],i]

            d[nums[i]] = i

        return [-1,-1]
        