class Solution:
    def removeDuplicates(self, nums: List[int]) -> int:
        insertIndex = 1
        for i in range(1, len(nums)):
            if nums[i - 1] != nums[i]:
                nums[insertIndex] = nums[i]

                insertIndex = insertIndex + 1

        return insertIndex
        