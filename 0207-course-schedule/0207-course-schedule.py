class Solution:
    def canFinish(self, numCourses: int, prerequisites: List[List[int]]) -> bool:
        adj = [[] for _ in range(numCourses)]
        indegree = [0] * numCourses
        for src,dst in prerequisites:
            adj[src].append(dst)
            indegree[dst] += 1

        queue = deque()
        for i in range(numCourses):
            if indegree[i] == 0:
                queue.append(i)

        finish = 0
        while queue:
            curr = queue.popleft()
            finish += 1
            for i in adj[curr]:
                indegree[i] -= 1
                if indegree[i] == 0:
                    queue.append(i)

        return finish == numCourses
        