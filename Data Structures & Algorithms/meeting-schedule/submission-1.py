"""
Definition of Interval:
class Interval(object):
    def __init__(self, start, end):
        self.start = start
        self.end = end
"""

class Solution:
    def canAttendMeetings(self, intervals: List[Interval]) -> bool:
        intervals.sort(key=lambda x: x.start)
        p1 = 0
        while (p1 < len(intervals) - 1):
            p2 = p1 + 1
            stb1 = intervals[p1]
            stb2 = intervals[p2]

            if stb2.start < stb1.end:
                return False
            p1 += 1
        return True