# Given a non-negative integer represented as a non-empty array of digits, plus one to the integer.
#
# You may assume the integer do not contain any leading zero, except the number 0 itself.
#
# The digits are stored such that the most significant digit is at the head of the list.

class Solution:
    def plusOne(self, digits):
        """
        :type digits: List[int]
        :rtype: List[int]
        """
        addition = 1
        for index in range(len(digits))[::-1]:
            res = digits[index] + addition
            digits[index] = res % 10
            addition = (int)(res / 10)
        if addition != 0:
            digits.insert(0, addition)
        return digits
