class Solution:
    def canFinish(self, numCourses: int, prerequisites: List[List[int]]) -> bool:
        indegree = [0] * numCourses
        adj = [[] for _ in range(numCourses)]
        finish = 0
        for src,dst in prerequisites:
            adj[src].append(dst)
            indegree[dst] += 1
        
        queue = deque()
        for i in range(numCourses):
            if indegree[i] == 0:
                queue.append(i)

        while queue:
            i = queue.popleft()
            finish += 1
            for d in adj[i]:
                indegree[d] -= 1
                if indegree[d] == 0:
                    queue.append(d)

        return finish == numCourses


        