class Solution:
    def permute(self, nums: List[int]) -> List[List[int]]:
        res = []
        used = set()
        def backtrack(curr) -> None:
            if len(curr) == len(nums):
                res.append(curr[:])
                return

            for num in nums:
                if num not in curr:
                    curr.append(num)
                    used.add(num)
                    
                    backtrack(curr)

                    used.remove(num)
                    curr.pop()

        backtrack([])
        return res
        