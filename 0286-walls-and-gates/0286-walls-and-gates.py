class Solution:
    def wallsAndGates(self, rooms: List[List[int]]) -> None:
        """
        Do not return anything, modify rooms in-place instead.
        """
        ROWS = len(rooms)
        COLS = len(rooms[0])
        queue = deque()
        dist = 0
        seen = set()

        for r in range(ROWS):
            for c in range(COLS):
                if rooms[r][c] == 0:
                    queue.append((r,c))
                    seen.add((r,c))

        def addRoom(r,c) -> None:
            if 0 <= r < ROWS and 0 <= c < COLS and (r,c) not in seen and rooms[r][c] != -1:
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

            dist+=1

        


        