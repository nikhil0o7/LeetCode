class Solution:
    def nextPermutation(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        i = len(nums) - 2
        # so find the next decreasing element
        while i >= 0 and nums[i + 1] <= nums[i]:
            i -= 1
        #Now make the smallest valid increase
        if i >= 0:
            j = len(nums) - 1
            while nums[j] <= nums[i]:
                j -= 1
            self.swap(nums,i,j)
        # now reverse the whole suffix since it's descending, you're gonna make it ascending
        self.reverse(nums, i + 1)


    def reverse(self,nums, start):
        i = start
        j = len(nums) - 1
        while i < j:
            self.swap(nums, i, j)
            i += 1
            j -= 1

    def swap(self, nums, i, j):
        temp = nums[i]
        nums[i] = nums[j]
        nums[j] = temp
