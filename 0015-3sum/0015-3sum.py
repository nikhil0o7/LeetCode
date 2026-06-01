class Solution:
    def threeSum(self, nums: list[int]) -> list[list[int]]:
        nums.sort()
        ans = []
        for i in range(len(nums) - 1):
            if nums[i] > 0:
                break
            elif i == 0 or nums[i - 1] != nums[i]:
                self.twoSum(nums,i,ans)

        return ans

    def twoSum(self, nums:list[int], i:int, ans:list[int]):
        l,r = i + 1, len(nums) - 1
        while l < r:
            t = nums[i] + nums[l] + nums[r]
            if t > 0:
                r -= 1
            elif t < 0:
                l += 1
            else:
                ans.append([nums[i],nums[l],nums[r]])
                l += 1
                r -= 1
                while l < r and nums[l - 1] == nums[l]:
                    l += 1

        