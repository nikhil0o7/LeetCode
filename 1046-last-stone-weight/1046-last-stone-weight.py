class Solution:
    def lastStoneWeight(self, stones: List[int]) -> int:
        heap = []
        heapq.heapify(heap)
        for stone in stones:
            heapq.heappush(heap, -stone)
        
        while len(heap) > 1:

            x = -heapq.heappop(heap)
            y = -heapq.heappop(heap)
            # print(x,y)
            if x == y:
                continue
            elif x != y:
                curr = x - y
                heapq.heappush(heap, -curr)

        return -heap[0] if heap else 0          