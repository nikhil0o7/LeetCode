class Solution:
    def minMeetingRooms(self, intervals: List[List[int]]) -> int:
        time = []
        for interval in intervals:
            time.append((interval[0], 1))
            time.append((interval[1], -1))

        time.sort()
        res = count = 0
        for t in time:
            count += t[1]
            res = max(count,res)


        return res
        