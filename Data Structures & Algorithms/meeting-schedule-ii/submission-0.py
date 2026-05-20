"""
Definition of Interval:
class Interval(object):
    def __init__(self, start, end):
        self.start = start
        self.end = end
"""

class Solution:
    def minMeetingRooms(self, intervals: List[Interval]) -> int:
        # at any given time, what's the MOST meetings happening at the same time

        intervals.sort(key=lambda i: i.start)
        min_heap = []
        for i in intervals: 
            # if heap is not empty AND the earliest end time is less than or equal 
            # to the current start time, we can use that room, so pop
            if min_heap and min_heap[0] <= i.start:
                heapq.heappop(min_heap)
            # otherwise, push this meeting's end time into the heap and occupy a room
            heapq.heappush(min_heap, i.end)
        # the size of the heap represents the min number of rooms in use
        return len(min_heap)
            

