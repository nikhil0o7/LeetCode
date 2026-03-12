class Solution:
    def findOrder(self, numCourses: int, prerequisites: List[List[int]]) -> List[int]:
        indegree = [0] * numCourses
        adj = [[] for i in range(numCourses)]
        for src,dst in prerequisites:
            indegree[dst] += 1
            adj[src].append(dst)

        q= deque()
        for i in range(numCourses):
            if indegree[i] == 0:
                q.append(i)

        output = []
        finish = 0
        while q:
            node = q.popleft()
            finish += 1
            output.append(node)
            for n in adj[node]:
                indegree[n] -=1
                if indegree[n] == 0:
                    q.append(n)     
        if finish != numCourses:
            return []

        return output[::-1]