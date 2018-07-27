# Given two non-negative integers num1 and num2 represented as strings, return the product of num1 and num2, also represented as a string.
#
# Example 1:
#
# Input: num1 = "2", num2 = "3"
# Output: "6"
# Example 2:
#
# Input: num1 = "123", num2 = "456"
# Output: "56088"
# Note:
#
# The length of both num1 and num2 is < 110.
# Both num1 and num2 contain only digits 0-9.
# Both num1 and num2 do not contain any leading zero, except the number 0 itself.
# You must not use any built-in BigInteger library or convert the inputs to integer directly.

class Solution(object):
    def multiply(self, num1, num2):
        """
        :type num1: str
        :type num2: str
        :rtype: str
        """
        l1, l2 = len(num1), len(num2)
        # special case
        if l1 == 0 or l2 == 0 or num1 == '0' or num2 == '0':
            return '0'
        if num1 == '1':
            return num2
        elif num2 == '1':
            return num1

        res = []
        carry, mult = 0, 0
        for idy, y in enumerate(num2[::-1]):
            for idx, x in enumerate(num1[::-1]):
                mult = (ord(x) - ord('0')) * (ord(y) - ord('0')) + carry
                carry = mult // 10
                if idy + idx == len(res):
                    res.append(str(mult % 10))
                else:
                    pre = ord(res[idy + idx]) - ord('0') + mult % 10
                    carry += (pre // 10)
                    res[idy + idx] = str(pre % 10)
            if carry != 0:
                res.append(str(carry))
                carry = 0
        res.reverse()
        return ''.join(res)


s = Solution()
print(s.multiply('123', '456'))
