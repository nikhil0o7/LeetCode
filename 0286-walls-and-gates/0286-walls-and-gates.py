class Solution:
    def wallsAndGates(self, rooms: List[List[int]]) -> None:
        """
        Do not return anything, modify rooms in-place instead.
        """
        ROWS = len(rooms)
        COLS = len(rooms[0])
        queue = deque()
        seen = set()
        dist = 0

        for r in range(ROWS):
            for c in range(COLS):
                if rooms[r][c] == 0:
                    queue.append((r,c))
                    seen.add((r,c))

        def addRoom(r,c):
            if (0 > r or r == ROWS or 0 > c or c == COLS or (r,c) in seen or rooms[r][c] == -1):
                return
            queue.append((r,c))
            seen.add((r,c))


        while queue:
            for i in range(len(queue)):
                r,c = queue.popleft()
                rooms[r][c] = dist
                addRoom(r + 1, c)
                addRoom(r - 1, c)
                addRoom(r, c + 1)
                addRoom(r, c - 1)
            dist += 1