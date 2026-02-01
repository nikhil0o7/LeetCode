class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        res , dups = set(), set()
        seen = {}
        for i in range(len(nums) - 1):
            if nums[i] not in dups:
                dups.add(nums[i])
            
                for j in range(i+1, len(nums)):
                    compliment = -nums[i] - nums[j]

                    if compliment in seen and seen[compliment] == i:
                        res.add(tuple(sorted((nums[i],nums[j],compliment))))
                    
                    seen[nums[j]] = i


        return [list(x) for x in res]