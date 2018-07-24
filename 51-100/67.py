# Given two binary strings, return their sum (also a binary string).
#
# For example,
# a = "11"
# b = "1"
# Return "100".

class Solution:
    def addBinary(self, a, b):
        """
        :type a: str
        :type b: str
        :rtype: str
        """
        la = len(a)
        lb = len(b)
        if la >= lb:
            length = la
        else:
            length = lb
        digits = []
        addition = 0
        for x in range(1, length + 1):
            if x > la:
                an = 0
            else:
                an = int(a[-x])
            if x > lb:
                bn = 0
            else:
                bn = int(b[-x])

            res = an + bn + addition
            if res == 3:
                digits.append("1")
                addition = 1
            elif res == 2:
                digits.append("0")
                addition = 1
            elif res == 1:
                digits.append("1")
                addition = 0
            elif res == 0:
                digits.append("0")
                addition = 0
        if addition != 0:
            digits.append(str(addition))
        digits.reverse()
        return "".join(digits)

s = Solution()
print(s.addBinary("0", "0"))
# print(s.addBinary("11", "1"))
