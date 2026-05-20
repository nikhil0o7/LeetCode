class Solution:
    def minimumFuelCost(self, roads: List[List[int]], seats: int) -> int:
        n = len(roads) + 1
        adj = defaultdict(list)
        degree = [0] * n

        for u,v in roads:
            adj[u].append(v)
            adj[v].append(u)

            degree[u] += 1
            degree[v] += 1

        q = deque()

        for i in range(1,n):
            if degree[i] == 1:
                q.append(i)
        rep = [1] * n
        fuel = 0

        while q:
            node = q.popleft()

            fuel += (rep[node] + seats - 1) // seats

            for neighbor in adj[node]:
                degree[neighbor] -= 1
                rep[neighbor] += rep[node]

                if degree[neighbor] == 1 and neighbor != 0:
                    q.append(neighbor)

        return fuel