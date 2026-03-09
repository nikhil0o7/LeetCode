class Solution:
    def minReorder(self, n: int, connections: List[List[int]]) -> int:
        roads = set()
        graph = defaultdict(list)
        for x,y in connections:
            graph[x].append(y)
            graph[y].append(x)
            roads.add((x,y))

        def dfs(node):
            ans = 0
            for neighbour in graph[node]:
                if neighbour not in seen:
                    if (node,neighbour) in roads:
                        ans += 1
                    seen.add(neighbour)
                    ans += dfs(neighbour)
            return ans

        seen = {0}
        return dfs(0)
        