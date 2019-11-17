"""
Given a collection of intervals, merge all overlapping intervals.
For example:
Given [1,3],[2,6],[8,10],[15,18],
return [1,6],[8,10],[15,18].
Make sure the returned intervals are sorted.
"""
class Interval:
    def __init__(self, s=0, e=0):
        self.start = s
        self.end = e

class Solution:
    # @param intervals, a list of Intervals
    # @return a list of Interval
    def merge(self, intervals):
        res = []
        for interval in sorted(intervals, key=lambda x: x.start):
            if res and interval.start <= res[-1].end:
                res[-1].end = max(interval.end, res[-1].end)
            else:
                res.append(interval)
        return res
