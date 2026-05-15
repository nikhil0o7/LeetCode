class Solution:
    def eventualSafeNodes(self, graph: List[List[int]]) -> List[int]:
        n = len(graph)
        adj = [[] for _ in range(n)]
        indegree = [0] * n
        # print(adj)
        for i in range(n):
            for node in graph[i]:
                adj[node].append(i)
                indegree[i] += 1

        q = deque()
        for i in range(n):
            if indegree[i] == 0:
                q.append(i)
        # print(indegree)
        safe = [False] * n
        while q:
            node = q.popleft()
            safe[node] = True

            for neighbor in adj[node]:
                indegree[neighbor] -= 1
                if indegree[neighbor] == 0: 
                    q.append(neighbor)

        # print(safe)
        safeEdges = []
        for i in range(n):
            if safe[i]:
                safeEdges.append(i)

        return safeEdges



        