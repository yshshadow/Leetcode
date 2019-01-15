# In a row of seats, 1 represents a person sitting in that seat, and 0 represents that the seat is empty.
#
# There is at least one empty seat, and at least one person sitting.
#
# Alex wants to sit in the seat such that the distance between him and the closest person to him is maximized.
#
# Return that maximum distance to closest person.
#
# Example 1:
#
# Input: [1,0,0,0,1,0,1]
# Output: 2
# Explanation:
# If Alex sits in the second open seat (seats[2]), then the closest person has distance 2.
# If Alex sits in any other open seat, the closest person has distance 1.
# Thus, the maximum distance to the closest person is 2.
# Example 2:
#
# Input: [1,0,0,0]
# Output: 3
# Explanation:
# If Alex sits in the last seat, the closest person is 3 seats away.
# This is the maximum distance possible, so the answer is 3.
# Note:
#
# 1 <= seats.length <= 20000
# seats contains only 0s or 1s, at least one 0, and at least one 1.

class Solution(object):
    def maxDistToClosest(self, seats):
        """
        :type seats: List[int]
        :rtype: int
        """
        p_index = []
        for i, seat in enumerate(seats):
            if seat == 1:
                p_index.append(i)
        i, j = 0, 0
        m = 0
        while i < len(seats):
            if j < len(p_index) - 1 and i > p_index[j + 1]:
                j += 1
            if seats[i] == 1:
                pass
            elif i < p_index[j]:
                m = max(m, p_index[j] - i)
            elif j == len(p_index) - 1 and i > p_index[j]:
                m = max(m, i - p_index[j])
            else:
                m = max(m, min(i - p_index[j], p_index[j + 1] - i))
            i += 1
        return m

s=Solution()
print(s.maxDistToClosest([1,0,0,0,1,0,1]))