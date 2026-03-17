class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        res = [0 for _ in range(len(nums))]
        prefix = 1
        for i in range(len(nums)):
            res[i] = prefix
            prefix = nums[i] * prefix
        # print(res)
        postfix = 1
        for i in range(len(nums) - 1, -1 , -1):
            res[i] = postfix * res[i]
            postfix = nums[i] * postfix
        # print(res)
        return res


        