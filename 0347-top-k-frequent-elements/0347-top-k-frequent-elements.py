class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        n = len(nums)
        buckets = [[] for i in range(len(nums) + 1)]
        countN = Counter(nums)

        for num,freq in countN.items():
            buckets[freq].append(num)

        ans = []
        for i in range(len(buckets) - 1, -1, -1):
            for num in buckets[i]:
                ans.append(num)
                k -= 1
                if k == 0:
                    return ans


