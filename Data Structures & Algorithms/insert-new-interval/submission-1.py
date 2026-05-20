class Solution:
    def insert(self, intervals: List[List[int]], newInterval: List[int]) -> List[List[int]]:
        # [[1,3],[4,6]]
        # [2,5]
            # 1,5
            # 1,6
            # reached end, return 1,6
        # [[1,6]]

        # [[1,2],[3,5],[9,10]]
        # [6,7]
            # attach 1,2 
            # attach 3,5
            # attach newInterval and add rest of list
        # [[1,2],[3,5],[6,7],[9,10]]
        res = []
        for i in range(len(intervals)):
            if newInterval[1] < intervals[i][0]:
                res.append(newInterval)
                return res + intervals[i:]
            if intervals[i][1] < newInterval[0]:
                res.append(intervals[i]) 
            else:
                newInterval = [
                    min(newInterval[0], intervals[i][0]),
                    max(newInterval[1], intervals[i][1]),
                ]
        res.append(newInterval)
        return res
        # If newInterval ends before the current interval starts, 
        # there will be no overlap with any later interval either.

        # If the current interval ends before newInterval starts, 
        # it can be added to the result unchanged.

        # If they overlap, we merge them by expanding newInterval 
        # to cover both ranges.




