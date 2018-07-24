# Given an integer (signed 32 bits), write a function to check whether it is a power of 4.
#
# Example:
# Given num = 16, return true. Given num = 5, return false.
#
# Follow up: Could you solve it without loops/recursion?


class Solution(object):
    def isPowerOfFour(self, num):
        """
        :type num: int
        :rtype: bool
        """
        # test = 1
        # while test < num:
        #     test << 2
        # return test == num
        if num == 1 or num == 4:
            return True
        if num % 4 != 0 or num < 1:
            return False
        return self.isPowerOfFour(num // 4)
