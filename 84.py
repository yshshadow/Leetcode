# Given n non-negative integers representing the histogram's bar height where the width of each bar is 1, find the area of largest rectangle in the histogram.
#
#
# Above is a histogram where width of each bar is 1, given height = [2,1,5,6,2,3].
#
#
# The largest rectangle is shown in the shaded area, which has area = 10 unit.
#
# For example,
# Given heights = [2,1,5,6,2,3],
# return 10.

class Solution(object):
    def largestRectangleArea(self, heights):
        """
        :type heights: List[int]
        :rtype: int
        """
        if not heights or len(heights) == 0:
            return 0
        if len(heights) == 1:
            return heights[0]
        begin, end = 0, len(heights) - 1
        max_area = 0

        while begin <= end:
            area = (end - begin + 1) * self.minHeight(heights, begin, end)
            max_area = max(area, max_area)
            if heights[begin] < heights[end]:
                begin += 1
            else:
                end -= 1
        return max_area

    def minHeight(self, heights, begin, end):
        min_height = heights[begin]
        for x in range(begin, end+1):
            min_height = min(min_height, heights[x])
        return min_height


s = Solution()
# print(s.largestRectangleArea([2, 1, 5, 6, 2, 3]))
# print(s.largestRectangleArea([0,9]))
print(s.largestRectangleArea([4,2,0,3,2,4,3,4]))
