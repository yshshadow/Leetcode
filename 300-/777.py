# In a string composed of 'L', 'R', and 'X' characters, like "RXXLRXRXL", a move consists of either replacing one occurrence of "XL" with "LX", or replacing one occurrence of "RX" with "XR". Given the starting string start and the ending string end, return True if and only if there exists a sequence of moves to transform one string to the other.
#
# Example:
#
# Input: start = "RXXLRXRXL", end = "XRLXXRRLX"
# Output: True
# Explanation:
# We can transform start to end following these steps:
# RXXLRXRXL ->
# XRXLRXRXL ->
# XRLXRXRXL ->
# XRLXXRRXL ->
# XRLXXRRLX
# Note:
#
# 1 <= len(start) = len(end) <= 10000.
# Both start and end will only consist of characters in {'L', 'R', 'X'}.
import itertools


class Solution(object):
    def canTransform(self, start, end):
        """
        :type start: str
        :type end: str
        :rtype: bool
        """
        # not work
        # if start == end:
        #     return True
        # start = list(start)
        #
        # while True:
        #     t = ''.join(start)
        #     i = 0
        #     while i < len(start) - 1:
        #         if start[i] == 'X' and start[i + 1] == 'L':
        #             start[i] = 'L'
        #             start[i + 1] = 'X'
        #             i += 1
        #         elif start[i] == 'R' and start[i + 1] == 'X':
        #             start[i] = 'X'
        #             start[i + 1] = 'R'
        #             i += 1
        #         i += 1
        #         if ''.join(start) == end:
        #             return True
        #     if t == ''.join(start):
        #         return False
        for (i, x), (j, y) in itertools.zip_longest(
                ((i, x) for i, x in enumerate(start) if x != 'X'),
                ((j, y) for j, y in enumerate(end) if y != 'X'),
                fillvalue=(None, None)):

            # If not solid or accessible, return False
            if x != y or (x == 'L' and i < j) or (x == 'R' and i > j):
                return False

        return True


s = Solution()
# print(s.canTransform('RXL', 'XRL'))
print(s.canTransform("XXXXXLXXXX",
                     "LXXXXXXXXX"))
