class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        count = Counter(nums)
        heap = [(-freq,num) for num,freq in count.items()]
        heapq.heapify(heap)
        ans = []
        for i in range(k):
            ans.append(heapq.heappop(heap)[1])
        return ans