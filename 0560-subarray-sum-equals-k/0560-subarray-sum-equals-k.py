class Solution:
    def subarraySum(self, nums: List[int], k: int) -> int:
        count = { 0 : 1 } # prefix sum zero one time (basically nothign)
        res, prefix= 0 , 0
        for i in range(len(nums)):
            prefix += nums[i]
            res += count.get(prefix - k, 0) 
            count[prefix] = count.get(prefix, 0) + 1
        return res
