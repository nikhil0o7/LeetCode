class Solution:
    def lastStoneWeight(self, stones: List[int]) -> int:
        heap = []
        heapq.heapify(heap)
        for stone in stones:
            heapq.heappush(heap, -stone)

        while heap and len(heap) > 1:

            x = heapq.heappop(heap)
            y = heapq.heappop(heap)


            if x == y:
                continue
            else:
                curr = abs(x - y)
                heapq.heappush(heap, -curr)

        return -heap[0] if heap else 0
            

        