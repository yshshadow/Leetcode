# Given n points on a 2D plane, find the maximum number of points that lie on the same straight line.
#
# Example 1:
#
# Input: [[1,1],[2,2],[3,3]]
# Output: 3
# Explanation:
# ^
# |
# |        o
# |     o
# |  o
# +------------->
# 0  1  2  3  4
# Example 2:
#
# Input: [[1,1],[3,2],[5,3],[4,1],[2,3],[1,4]]
# Output: 4
# Explanation:
# ^
# |
# |  o
# |     o        o
# |        o
# |  o        o
# +------------------->
# 0  1  2  3  4  5  6

# Definition for a point.
import collections
from fractions import Fraction


class Point(object):
    def __init__(self, a=0, b=0):
        self.x = a
        self.y = b


class Solution(object):
    def maxPoints(self, points):
        """
        :type points: List[Point]
        :rtype: int
        """
        if len(points) == 0:
            return 0
        if len(points) == 1:
            return 1

        kv = {}
        for pi in range(len(points)):
            for pj in range(pi + 1, len(points)):
                i = points[pi]
                j = points[pj]
                if i == j:
                    continue
                if i.x == j.x:
                    t = ('-', i.x)
                else:
                    k = Fraction(i.y - j.y, i.x - j.x)
                    b = Fraction(i.x * j.y - j.x * i.y, i.x - j.x)
                    t = (k, b)
                if t not in kv:
                    kv[t] = [i, j]
                else:
                    if i not in kv[t]:
                        kv[t].append(i)
                    if j not in kv[t]:
                        kv[t].append(j)
        return max([len(v) for v in kv.values()])


def prc(points):
    return [Point(point[0], point[1]) for point in points]


s = Solution()
print(s.maxPoints(prc(
    [[0, 0], [94911151, 94911150], [94911152, 94911151]]
)))
# print(s.maxPoints([Point(0, 0), Point(3, 2), Point(0, 0)]))
# print(s.maxPoints([Point(1, 1), Point(2, 2), Point(3, 3)]))
# print(s.maxPoints([Point(1, 1), Point(3, 2), Point(5, 3), Point(4, 1), Point(2, 3), Point(1, 4)]))
