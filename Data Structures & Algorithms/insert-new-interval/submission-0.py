class Solution:
    def insert(self, intervals: List[List[int]], newInterval: List[int]) -> List[List[int]]:
        # [[1,3],[4,6]]
        # [2,5]
        # [[1,6]]

        # [[1,2],[3,5],[9,10]]
        # [6,7]
        # [[1,2],[3,5],[6,7],[9,10]]

        res = []
        # If newInterval ends before the current interval starts, 
        # there will be no overlap with any later interval either.

        # If the current interval ends before newInterval starts, 
        # it can be added to the result unchanged.

        # If they overlap, we merge them by expanding newInterval 
        # to cover both ranges.

        for i in range(len(intervals)):
            if newInterval[1] < intervals[i][0]: 
                res.append(newInterval)
                return res + intervals[i:] # this means we attach new interval to res and return all remaining intervals 
            elif newInterval[0] > intervals[i][1]:
                res.append(intervals[i]) # this means current interval is well before newInerval
            else: # there's overlap, make the new interval contain both intervals
                newInterval = [
                    min(newInterval[0], intervals[i][0]),
                    max(newInterval[1], intervals[i][1]),
                ]
        res.append(newInterval) # if we nade it this far, we append new interval to the end and return res
        return res


