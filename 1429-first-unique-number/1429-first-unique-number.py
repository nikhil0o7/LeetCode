from collections import deque
from typing import List

class FirstUnique:

    def __init__(self, nums: List[int]):
        self._isUnique = {}
        self._queue = deque()

        for num in nums:
            self.add(num)

    def showFirstUnique(self) -> int:
        while self._queue and not self._isUnique[self._queue[0]]:
            self._queue.popleft()

        if self._queue:
            return self._queue[0]

        return -1

    def add(self, value: int) -> None:
        if value not in self._isUnique:
            self._queue.append(value)
            self._isUnique[value] = True
        else:
            self._isUnique[value] = False