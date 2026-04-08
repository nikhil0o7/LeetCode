class Solution:
    def threeSum(self, nums: list[int]) -> list[list[int]]:
        nums.sort()
        res = []
        for i in range(len(nums)):
            if nums[i] > 0:
                break
            elif i == 0 or nums[i - 1] != nums[i]:
                self.twoSum(nums, i , res)

        return res

    def twoSum(self, nums, i, res):
        l, r = i + 1 , len(nums) - 1
        while l < r:
            s = nums[i] + nums[l] + nums[r]
            if s < 0:
                l += 1
            elif s > 0:
                r -= 1
            else:
                res.append([nums[i], nums[l], nums[r]])
                l+=1
                r-=1
                while l < r and nums[l - 1] == nums[l]:
                    l +=1

