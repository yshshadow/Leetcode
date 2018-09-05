# Given an integer, write a function to determine if it is a power of three.
#
# Example 1:
#
# Input: 27
# Output: true
# Example 2:
#
# Input: 0
# Output: false
# Example 3:
#
# Input: 9
# Output: true
# Example 4:
#
# Input: 45
# Output: false
# Follow up:
# Could you do it without using any loop / recursion?

class Solution(object):
    def isPowerOfThree(self, n):
        """
        :type n: int
        :rtype: bool
        """
        if n == 1:
            return True
        elif n<1 or n % 3 != 0:
            return False
        return self.isPowerOfThree(int(n / 3))


s = Solution()
print(s.isPowerOfThree(45))
