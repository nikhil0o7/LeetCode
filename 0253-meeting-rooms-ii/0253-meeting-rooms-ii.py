class Solution:
    def minMeetingRooms(self, intervals: List[List[int]]) -> int:
        time = []
        for i in intervals:
            time.append((i[0],1))
            time.append((i[1], -1))

        time.sort(key=lambda x: (x[0], x[1]))

        res = count = 0
        for t in time:
            count += t[1]
            res = max(res,count)

        return res
        