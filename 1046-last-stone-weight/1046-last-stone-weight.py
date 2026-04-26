class Solution:
    def lastStoneWeight(self, stones: List[int]) -> int:
        heap = []
        heapq.heapify(heap)
        for stone in stones:
            heapq.heappush(heap, -stone)
        while len(heap) > 1:
            x = heapq.heappop(heap)
            y = heapq.heappop(heap)
            if x == y:
                continue
            elif x!=y:
                s = x - y
                heapq.heappush(heap,s)

        return -heap[0] if len(heap) > 0 else 0