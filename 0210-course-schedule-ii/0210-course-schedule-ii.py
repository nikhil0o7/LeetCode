from collections import deque

class Solution:
    def findOrder(self, numCourses: int, prerequisites: List[List[int]]) -> List[int]:
        adj = [[] for _ in range(numCourses)]
        indegree = [0] * numCourses
        print(adj)
        queue = deque()
        for src,dst in prerequisites:
            adj[src].append(dst)
            indegree[dst] += 1

        for i in range(numCourses):
            if indegree[i] == 0:
                queue.append(i)

        if not queue:
            return []
        order = []
        while queue:
            curr = queue.popleft()
            order.append(curr)
            for nei in adj[curr]:
                indegree[nei] -= 1
                if indegree[nei] == 0:
                    queue.append(nei)


        return order[::-1] if len(order) == numCourses else []        