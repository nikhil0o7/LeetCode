class Solution:
    def findCircleNum(self, isConnected: List[List[int]]) -> int:
        graph = defaultdict(list)
        n = len(isConnected)
        for i in range(n):
            for j in range(i + 1, n):
                if isConnected[i][j]:
                    graph[i].append(j)
                    graph[j].append(i)
        seen = set()
        ans = 0 
        def dfs(node):
            for neighbour in graph[node]:
                if neighbour not in seen:
                    seen.add(neighbour)
                    dfs(neighbour)

        for i in range(n):
            if i not in seen:
                seen.add(i)
                ans += 1
                dfs(i)


        return ans