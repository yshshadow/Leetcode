# Given n non-negative integers a1, a2, ..., an, where each represents a point at coordinate (i, ai). n vertical lines are drawn such that the two endpoints of line i is at (i, ai) and (i, 0). Find two lines, which together with x-axis forms a container, such that the container contains the most water.
#
# Note: You may not slant the container and n is at least 2.

class Solution(object):
    def maxArea(self, height):
        """
        :type height: List[int]
        :rtype: int
        """
        begin, end = 0, len(height)-1
        max_area = 0
        while begin < end:
            area = (end - begin) * min(height[begin], height[end])
            max_area = max(max_area, area)
            if height[begin] <= height[end]:
                begin += 1
            else:
                end -= 1
        return max_area

s = Solution()
s.maxArea([1,1])