# Given n points in the plane that are all pairwise distinct, a "boomerang" is a tuple of points (i, j, k) such that the distance between i and j equals the distance between i and k (the order of the tuple matters).
#
# Find the number of boomerangs. You may assume that n will be at most 500 and coordinates of points are all in the range [-10000, 10000] (inclusive).
#
# Example:
# Input:
# [[0,0],[1,0],[2,0]]
#
# Output:
# 2
#
# Explanation:
# The two boomerangs are [[1,0],[0,0],[2,0]] and [[1,0],[2,0],[0,0]]

class Solution(object):
    def numberOfBoomerangs(self, points):
        """
        :type points: List[List[int]]
        :rtype: int
        """
        res = 0
        for i in range(len(points)):
            hashmap = {}
            for j in range(len(points)):
                dist = self.distance(points[i], points[j])
                if dist in hashmap:
                    res += hashmap[dist] * 2
                    hashmap[dist] += 1
                else:
                    hashmap[dist] = 1
        return res

    def distance(self, a, b):
        return (a[0] - b[0]) ** 2 + (a[1] - b[1]) ** 2

s=Solution()
s.numberOfBoomerangs([[0,0],[1,0],[2,0]])