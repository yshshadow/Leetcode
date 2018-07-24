# Implement pow(x, n).
#
#
# Example 1:
#
# Input: 2.00000, 10
# Output: 1024.00000
# Example 2:
#
# Input: 2.10000, 3
# Output: 9.26100

class Solution(object):
    def myPow(self, x, n):
        """
        :type x: float
        :type n: int
        :rtype: float
        """
        if not n:
            return 1
        elif n < 0:
            return 1 / self.myPow(x, -n)
        elif n % 2:
            return x * self.myPow(x, n - 1)
        else:
            return self.myPow(x * x, n / 2)


s = Solution()
# print(s.myPow(2.00000, 10))
# print(s.myPow(2.10000, 3))
print(s.myPow(34.00515, -3))
print(pow(34.00515, -3))
