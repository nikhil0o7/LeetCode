class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        n = len(nums)
        buckets = [[] for _ in range(n + 1)]
        countN = Counter(nums)

        for num,freq in countN.items():
            buckets[freq].append(num)

        ans = []
        for i in range(len(buckets) - 1, -1, -1):
            for n in buckets[i]:
                if k > 0:
                    ans.append(n)
                    k -=1

        return ans



