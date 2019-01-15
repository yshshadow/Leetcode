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
        # O(n^3) brute force, tle
        # if not heights:
        #     return 0
        # globa = 0
        # for i, height in enumerate(heights):
        #     local = height
        #     for j in range(i):
        #         minheight = min(heights[j:i + 1])
        #         local = max(local, minheight * (i - j + 1))
        #     globa = max(globa, local)
        # return globa

        # O(n^2) brute force, tle
        # if not heights:
        #     return 0
        # globa = 0
        # l = len(heights)
        # for i in range(l):
        #     minheight = 2147483647
        #     for j in range(i, l):
        #         minheight = min(minheight, heights[j])
        #         globa = max(globa, minheight * (j - i + 1))
        # return globa

        # divide and conquer , tle
        # if not heights:
        #     return 0
        #
        # def helper(start, end):
        #     if start > end:
        #         return 0
        #     minindex = start
        #     for i in range(start, end + 1):
        #         if heights[i] < heights[minindex]:
        #             minindex = i
        #     l_area = helper(start, minindex - 1)
        #     r_area = helper(minindex + 1, end)
        #     return max(heights[minindex] * (end - start + 1), l_area, r_area)
        #
        # return helper(0, len(heights) - 1)

        # stack
        if not heights:
            return 0
        stack = [-1]
        res = 0
        for i, h in enumerate(heights):
            while stack[-1] != -1 and heights[stack[-1]] < h:
                cur = stack.pop()
                res = max(res, heights[cur] * (i - stack[-1] - 1))
            stack.append(i)
        while stack[-1] != -1:
            cur = stack.pop()
            res = max(res, heights[cur] * (len(heights) - stack[-1] - 1))
        return res


s = Solution()
# print(s.largestRectangleArea([2, 1, 5, 6, 2, 3]))
# print(s.largestRectangleArea([0,9]))
print(s.largestRectangleArea([4, 2, 0, 3, 2, 4, 3, 4]))
