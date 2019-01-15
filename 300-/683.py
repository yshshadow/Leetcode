# There is a garden with N slots. In each slot, there is a flower. The N flowers will bloom one by one in N days. In each day, there will be exactly one flower blooming and it will be in the status of blooming since then.
#
# Given an array flowers consists of number from 1 to N. Each number in the array represents the place where the flower will open in that day.
#
# For example, flowers[i] = x means that the unique flower that blooms at day i will be at position x, where i and x will be in the range from 1 to N.
#
# Also given an integer k, you need to output in which day there exists two flowers in the status of blooming, and also the number of flowers between them is k and these flowers are not blooming.
#
# If there isn't such day, output -1.
#
# Example 1:
# Input:
# flowers: [1,3,2]
# k: 1
# Output: 2
# Explanation: In the second day, the first and the third flower have become blooming.
# Example 2:
# Input:
# flowers: [1,2,3]
# k: 1
# Output: -1
# Note:
# The given array will be in the range [1, 20000].
import bisect


class Solution(object):
    def kEmptySlots(self, flowers, k):
        """
        :type flowers: List[int]
        :type k: int
        :rtype: int
        """
        if not flowers:
            return -1
        pos = [flowers[0]]
        for i, p in enumerate(flowers[1:]):
            insert_pos = bisect.bisect_left(pos, p)
            if (insert_pos == 0 and pos[0] - p - 1 == k) or (insert_pos == len(pos) and p - pos[-1] - 1 == k):
                return i + 2
            elif insert_pos < len(pos) and (pos[insert_pos] - p - 1 == k or p - pos[insert_pos - 1] - 1 == k):
                return i + 2
            pos.insert(insert_pos, p)
        return -1


s = Solution()
# print(s.kEmptySlots([6, 5, 8, 9, 7, 1, 10, 2, 3, 4],
#                     2))
print(s.kEmptySlots([9, 1, 4, 2, 8, 7, 5, 3, 6, 10],
                    3))
print(s.kEmptySlots([1, 3, 2], 1))
