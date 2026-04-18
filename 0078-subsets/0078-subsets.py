class Solution:
    def subsets(self, nums: List[int]) -> List[List[int]]:
        res = []

        def backtrack(i, curr):
                
            if i > len(nums):
                return
            res.append(curr[:])
            for j in range(i, len(nums)):
                curr.append(nums[j])
                backtrack(j + 1, curr)
                curr.pop()

        backtrack(0, [])
        return res

        