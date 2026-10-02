"""
Definition of Interval:
class Interval(object):
    def __init__(self, start, end):
        self.start = start
        self.end = end
"""

class Solution:
    def minMeetingRooms(self, intervals: List[Interval]) -> int:
        # start to end 1          start to end 4
                # start to end 2
                    # start to end 3 
        start = [interval.start for interval in intervals]
        end = [interval.end for interval in intervals]
        start.sort()
        end.sort()
        l = 0
        res = 0
        curr =0
        for r in range(len(intervals)):
            while l < len(intervals) and start[l] < end[r]:
                curr += 1
                l += 1
            res = max(curr,res)
            curr -= 1
        return res
