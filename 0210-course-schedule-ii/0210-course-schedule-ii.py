class Solution:
    def findOrder(self, numCourses: int, prerequisites: List[List[int]]) -> List[int]:
        indegree = [0] * numCourses
        adj = [[] for i in range(numCourses)]
        for src,dst in prerequisites:
            indegree[dst] += 1
            adj[src].append(dst)
        print(adj)
        queue = deque()
        for i in range(numCourses):
            if indegree[i] == 0:
                queue.append(i)

        finish, output = 0, []

        while queue:
            node = queue.popleft()
            output.append(node)
            finish += 1
            for nei in adj[node]:
                indegree[nei] -= 1
                if indegree[nei] == 0:
                    queue.append(nei)
        
        if finish != numCourses:
            return []

        return output[::-1]