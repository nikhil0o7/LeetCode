class Solution:
    def subsetsWithDup(self, nums: List[int]) -> List[List[int]]:
        def backtrack(curr, i):
            if i == len(nums):
                ans.append(curr[:])
                return
            
            curr.append(nums[i])
            backtrack(curr, i + 1)
            curr.pop()

            while i + 1 < len(nums) and nums[i] == nums[i + 1]:
                i += 1
            backtrack(curr, i + 1)

        ans = []
        backtrack([],0)
        return ans