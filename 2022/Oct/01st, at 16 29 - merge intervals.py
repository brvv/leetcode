class Solution:
    def merge(self, intervals: List[List[int]]) -> List[List[int]]:
        sorted_intervals = sorted(intervals, key=lambda interval: interval[0])
        res = [sorted_intervals[0]]
        
        if len(sorted_intervals) == 1:
            return res
        
        for interval in sorted_intervals[1::]:
            start = interval[0]
            end = interval[1]
            
            last_interval = res[-1]
            last_interval_start = last_interval[0]
            last_interval_end = last_interval[1]
            
            if start > last_interval_end:
                res.append(interval)
            elif start <= last_interval_end and end >= last_interval_end:
                res[-1][1] = end
        return res
            