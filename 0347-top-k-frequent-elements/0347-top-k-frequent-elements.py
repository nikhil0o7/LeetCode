class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        buckets = [[] for _ in range(len(nums) + 1)]
        count_N = Counter(nums)
        for num, freq in count_N.items():
            buckets[freq].append(num)
        ans = []
        for i in range(len(buckets) - 1, -1 , -1):
            for num in buckets[i]:
                ans.append(num)
                if len(ans) == k:
                    return ans
        