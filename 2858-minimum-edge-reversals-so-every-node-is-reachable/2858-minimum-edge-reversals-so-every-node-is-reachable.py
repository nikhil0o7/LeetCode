class Solution:
    def minEdgeReversals(self, n: int, edges: List[List[int]]) -> List[int]:
        graph = defaultdict(list)

        for u, v in edges:
            graph[u].append((v, 0))  # correct direction from u to v
            graph[v].append((u, 1))  # would need reversal

        res = [0] * n

        def dfs_count(node, parent):
            reversals = 0

            for nei, cost in graph[node]:
                if nei == parent:
                    continue
                reversals += cost + dfs_count(nei, node)

            return reversals

        res[0] = dfs_count(0, -1)
        print(graph)
        print(res)
        def reroot(node, parent):
            for nei, cost in graph[node]:
                if nei == parent:
                    continue

                if cost == 0:
                    # Edge node -> nei was good for node as root.
                    # If nei becomes root, this edge becomes bad.
                    res[nei] = res[node] + 1
                else:
                    # Edge nei -> node was bad for node as root.
                    # If nei becomes root, this edge becomes good.
                    res[nei] = res[node] - 1

                reroot(nei, node)

        reroot(0, -1)

        return res