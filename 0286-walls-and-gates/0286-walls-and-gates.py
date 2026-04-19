class Solution:
    def wallsAndGates(self, rooms: List[List[int]]) -> None:
        ROWS, COLS = len(rooms),len(rooms[0])
        visit = set()
        q = deque()

        #first let's add all our gates to the queue and visit set
        for r in range(ROWS):
            for c in range(COLS):
                if rooms[r][c] == 0:
                    q.append([r,c])
                    visit.add((r,c))

        def addRoom(r,c):
            if(r < 0 or r == ROWS or c < 0 or c == COLS or (r,c) in visit or rooms[r][c] == -1):
                return
            visit.add((r,c))
            q.append([r,c])
        dist = 0
        while q:
            for i in range(len(q)):
                r,c = q.popleft()
                #labelling the min dist for that room
                rooms[r][c] = dist
                #adding all the four adjacent rooms to the queue
                addRoom(r + 1,c)
                addRoom(r - 1,c)
                addRoom(r,c + 1)
                addRoom(r,c - 1)
            dist += 1