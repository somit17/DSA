class Solution:
    def eraseOverlapIntervals(self, intervals: list[list[int]]) -> int:
        intervals.sort(key = lambda x : x[1])
        removed = 0
        last_end = float('-inf')
        for s,e in intervals:
            if s < last_end:
                removed+=1
            else:
                last_end = e
        return removed
        