# Given a set of non-overlapping intervals, insert a new interval into the intervals (merge if necessary).
#
# You may assume that the intervals were initially sorted according to their start times.
#
# Example 1:
#
# Input: intervals = [[1,3],[6,9]], newInterval = [2,5]
# Output: [[1,5],[6,9]]
# Example 2:
#
# Input: intervals = [[1,2],[3,5],[6,7],[8,10],[12,16]], newInterval = [4,8]
# Output: [[1,2],[3,10],[12,16]]
# Explanation: Because the new interval [4,8] overlaps with [3,5],[6,7],[8,10].


# Definition for an interval.
class Interval(object):
    def __init__(self, s=0, e=0):
        self.start = s
        self.end = e


class Solution(object):
    def insert(self, intervals, newInterval):
        """
        :type intervals: List[Interval]
        :type newInterval: Interval
        :rtype: List[Interval]
        """

        # first solution, use merge interval (no.56)
        # intervals.append(newInterval)
        # intervals.sort(key=lambda x: x.start)
        # merged = []
        #
        # for interval in intervals:
        #     if len(merged) == 0 or merged[-1].end < interval.start:
        #         merged.append(interval)
        #     else:
        #         merged[-1].end = max(merged[-1].end, interval.end)
        # return merged
        #
        #
        # use binary search
        def search(intervals, val):
            # find the position val < intervals[i].start
            i, j = 0, len(intervals) - 1
            while i <= j:
                mid = (i + j) // 2
                if intervals[mid].start > val:
                    j = mid
                else:
                    i = mid + 1
            return i

        left, right = newInterval.start, newInterval.end
        l, r = search(intervals, left), search(intervals, right)  # find left and right location using binary search
        if l > 0 and intervals[
                    l - 1].end >= left:  # new interval and left previous have interval, merge two interval,position-1
            l -= 1
            left = intervals[l].start
        if r > 0 and intervals[r - 1].end > right:  # new interval and right previous have interval, merge
            right = intervals[r - 1].end
        intervals[l:r] = [Interval(left, right)]  # replace interval
        return intervals


s = Solution()
s.insert([Interval(1, 5)], Interval(6, 8))
