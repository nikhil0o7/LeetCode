class Solution:
    def wallsAndGates(self, rooms: List[List[int]]) -> None:
        """
        Do not return anything, modify rooms in-place instead.
        """
        ROWS = len(rooms)
        COLS = len(rooms[0])
        queue = deque()
        seen = set()
        
        for r in range(ROWS):
            for c in range(COLS):
                if rooms[r][c] == 0:
                    queue.append((r,c))
                    seen.add((r,c))
        dist = 0

        def addRoom(curr_r,curr_c):
            if 0 <= curr_r < ROWS and 0 <= curr_c < COLS and (curr_r,curr_c) not in seen and rooms[curr_r][curr_c] != -1:
                seen.add((curr_r,curr_c))
                queue.append([curr_r,curr_c])

        while queue:
            for i in range(len(queue)):
                r,c = queue.popleft()
                rooms[r][c] = dist
                addRoom(r + 1,c)
                addRoom(r - 1,c)
                addRoom(r, c + 1)
                addRoom(r, c - 1)

            dist += 1
