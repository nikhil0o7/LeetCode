class Solution:
    def isPossibleDivide(self, nums: List[int], k: int) -> bool:
        if len(nums) % k:
            return False

        nums.sort()
        count = Counter(nums)
        for num in nums:
            if count[num]:
                for i in range(num, num + k):
                    if not count[i]:
                        return False
                    count[i] -=1
        return True        