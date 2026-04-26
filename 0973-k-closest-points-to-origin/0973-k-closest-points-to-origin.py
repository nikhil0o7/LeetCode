class Solution:
    def kClosest(self, points: List[List[int]], k: int) -> List[List[int]]:
        heap = []
        for i in range(k):
            heap.append((-self.squared_distance(points[i]),i))

        heapq.heapify(heap)
        for i in range(k, len(points)):
            curr = -self.squared_distance(points[i])
            if curr > heap[0][0]:
                heapq.heappushpop(heap,(curr,i))

        return [points[i] for (_ ,i) in heap]


    def squared_distance(self, point: List[int]) -> int:
        return point[0] ** 2 + point[1] **2
        