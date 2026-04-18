class Solution:
    def subsetsWithDup(self, nums: List[int]) -> List[List[int]]:
        
        def backtrack(curr,i):
            if i == len(nums):
                res.append(curr[:])
                return
            
            if i > len(nums):
                return 

            curr.append(nums[i])
            backtrack(curr, i + 1)
            curr.pop()

            while i < len(nums) - 1 and nums[i + 1] == nums[i]:
                i += 1

            backtrack(curr, i + 1)
            

        res = []
        backtrack([], 0)
        return res





        