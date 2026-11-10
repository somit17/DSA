class Solution:
    def merge(self, intervals: list[list[int]]) -> list[list[int]]:
        sorted_intervals = sorted(intervals,key = lambda x:x[0])
        combined = [sorted_intervals[0]]
        #default = 
        for current_interval in sorted_intervals:
            s2,e2 = current_interval
            s1,e1 = combined[-1]
            if e1 >= s2:
                if e2 > e1:
                    combined[-1] = (s1,e2)
            else:
                combined.append(current_interval)
        return combined
