"""
Definition of Interval:
class Interval(object):
    def __init__(self, start, end):
        self.start = start
        self.end = end
"""

class Solution:
    def canAttendMeetings(self, intervals: List[Interval]) -> bool:
        if len(intervals) <= 1:
            return True
        
        intervals.sort(key=lambda i: i.start)

        curr_end = intervals[0].end

        for i in range(1, len(intervals)):
            if intervals[i].start >= curr_end:
                curr_end = intervals[i].end
            else:
                return False
        return True

