class Solution:
    def merge(self, intervals: List[List[int]]) -> List[List[int]]:
        merged = []
        intervals.sort()
        for interval in intervals:
            if not merged or interval[0] > merged[-1][1]:
                merged.append(interval)

            else:
                merged[-1][1] = max(interval[1], merged[-1][1])

        return merged
        