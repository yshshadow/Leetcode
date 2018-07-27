# The count-and-say sequence is the sequence of integers with the first five terms as following:
#
# 1.     1
# 2.     11
# 3.     21
# 4.     1211
# 5.     111221
# 1 is read off as "one 1" or 11.
# 11 is read off as "two 1s" or 21.
# 21 is read off as "one 2, then one 1" or 1211.
# Given an integer n, generate the nth term of the count-and-say sequence.
#
# Note: Each term of the sequence of integers will be represented as a string.
#
# Example 1:
#
# Input: 1
# Output: "1"
# Example 2:
#
# Input: 4
# Output: "1211"

class Solution(object):
    def countAndSay(self, n):
        """
        :type n: int
        :rtype: str
        """
        if n == 0:
            return '1'
        res = '1'
        while n > 1:
            res = self.count(res)
            n -= 1
        return res

    def count(self, string):
        res = ''
        cur = ''
        num = 0
        for char in string:
            if char != cur:
                if num != 0:
                    res += (str(num) + cur)  # add number when current num change
                cur = char
                num = 1
            else:
                num += 1
        res += (str(num) + cur)  # add the last number
        return res


s = Solution()
print(s.countAndSay(2))
