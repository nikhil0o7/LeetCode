class Solution:
    def findOrder(self, numCourses: int, prerequisites: List[List[int]]) -> List[int]:
        adj = [[] for _ in range(numCourses)]
        indegree = [0] * numCourses
        for src,dst in prerequisites:
            adj[src].append(dst)
            indegree[dst] +=1

        queue = deque()
        for i in range(numCourses):
            if indegree[i] == 0:
                queue.append(i)

        order = []
        while queue:
            curr = queue.popleft()
            order.append(curr)
            for i in adj[curr]:
                indegree[i] -=1
                if indegree[i] == 0:
                    queue.append(i)
        
        return order[::-1] if len(order) == numCourses else []        

        