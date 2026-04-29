class Solution:
    def canPartition(self, nums: List[int]) -> bool:
        if sum(nums) % 2:
            return False

        dp = set()
        dp.add(0)
        target = sum(nums) // 2
        print(target)
        for i in range(len(nums) - 1, -1, -1):
            nextDP = set()
            
            for t in dp:
                if (t + nums[i]) == target:
                    print(dp)
                    return True
                nextDP.add(t + nums[i])
                nextDP.add(t)
            dp = nextDP

        print(target)
        print(dp)
        return True if target in dp else False