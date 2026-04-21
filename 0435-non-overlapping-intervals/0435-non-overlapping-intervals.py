class Solution:
    def eraseOverlapIntervals(self, intervals: List[List[int]]) -> int:
        intervals.sort()
        prev = intervals[0][1]
        ans = 0

        for interval in intervals[1:]:
            if interval[0] >= prev:
                prev = interval[1]
            else:
                ans += 1
                prev = min(interval[1],prev)

        return ans


        