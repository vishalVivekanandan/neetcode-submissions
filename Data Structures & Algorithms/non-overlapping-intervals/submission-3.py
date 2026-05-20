class Solution:
    def eraseOverlapIntervals(self, intervals: List[List[int]]) -> int:
        intervals.sort(key = lambda i : i[0])
        curr_end = intervals[0][1] 
        count = 0
        for start, end in intervals[1:]:
            if start < curr_end:
                count+=1
                curr_end = min(curr_end, end)
            else:
                curr_end = end
        return count