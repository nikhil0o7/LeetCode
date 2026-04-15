class Solution:
    def findKthLargest(self, nums, k):
        heap = []
        heapq.heapify(heap)
        for num in nums:
            heapq.heappush(heap, num)
            if len(heap) > k:
                heapq.heappop(heap)

        return heap[0]