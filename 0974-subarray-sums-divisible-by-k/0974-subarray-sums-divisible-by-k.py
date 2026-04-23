class Solution:
    def subarraysDivByK(self, nums: List[int], k: int) -> int:
        prefix_sum = 0
        result = 0
        prefix_map = {0 : 1}
        for num in nums:
            prefix_sum += num
            mod = prefix_sum % k
            result += prefix_map.get(mod, 0)
            prefix_map[mod] = prefix_map.get(mod, 0) + 1

        return result