"""
Definition of Interval:
class Interval(object):
    def __init__(self, start, end):
        self.start = start
        self.end = end
"""

class Solution:
    def canAttendMeetings(self, intervals: List[Interval]) -> bool:
        if not intervals:
            return True
        # sort by key
        intervals.sort(key=lambda i: i.start)
        
        # put 1st pair's val in current_end var
        current_end = intervals[0].end
        # for key, val in intervals[1:]
        for i in range(1, len(intervals)):
            if current_end <= intervals[i].start:
                current_end = intervals[i].end
            else:
                return False
        return True
            # if current_end val is less than or equal to val
                # reassign current_end to end
            # else return false
        # return true
            
