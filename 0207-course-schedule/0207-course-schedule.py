class Solution:
    def canFinish(self, numCourses: int, prerequisites: List[List[int]]) -> bool:
        indegree = [0] * numCourses
        adj = [[] for i in range(numCourses)]
        for src,dst in prerequisites:
            indegree[dst] += 1
            adj[src].append(dst)
        q = deque()
        for i in range(numCourses):
            if indegree[i] == 0:
                q.append(i)
        finish = 0
        while q:
            curr = q.popleft()
            finish += 1
            for n in adj[curr]:
                indegree[n] -= 1
                if indegree[n] == 0:
                    q.append(n)

        return finish == numCourses





        