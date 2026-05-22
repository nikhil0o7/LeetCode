class Solution:
    def numBusesToDestination(self, routes: List[List[int]], source: int, target: int) -> int:
        #multi source BFS
        if source == target:
            return 0
        n = len(routes)
        adj = defaultdict(list)
        # create a adj list of stops to bus routes
        for r in range(n):
            for stop in routes[r]:
                adj[stop].append(r)

        # print(adj)
        if source not in adj or target not in adj:
            return -1

        queue = deque()
        seen = set()

        # now starting points are all routes which have source as a stop
        for route in adj[source]:
            queue.append(route)
            seen.add(route)

        busCount = 1

        # now start from all the avilable source routes, go to next station and if one of the route has the target means you're able to reach the destination
        while queue:
            size = len(queue)

            for _ in range(size):
                route = queue.popleft()

                for stop in routes[route]:
                    if stop == target:
                        return busCount

                    for nextRoute in adj[stop]:
                        if nextRoute not in seen:
                            seen.add(nextRoute)
                            queue.append(nextRoute)

            busCount += 1
        return -1
        
        