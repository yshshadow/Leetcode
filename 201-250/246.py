# A strobogrammatic number is a number that looks the same when rotated 180 degrees (looked at upside down).
#
# Write a function to determine if a number is strobogrammatic. The number is represented as a string.
#
# Example 1:
#
# Input:  "69"
# Output: true
# Example 2:
#
# Input:  "88"
# Output: true
# Example 3:
#
# Input:  "962"
# Output: false

class Solution(object):
    rotate = {'0': '0', '1': '1', '6': '9', '9': '6', '8': '8'}

    def isStrobogrammatic(self, num):
        """
        :type num: str
        :rtype: bool
        """
        r = list(reversed(num))
        for i in range(len(r)):
            if r[i] not in self.rotate:
                return False
            else:
                r[i] = self.rotate[r[i]]
        return ''.join(r) == num
