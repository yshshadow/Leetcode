# Determine whether an integer is a palindrome. Do this without extra space.
#
# click to show spoilers.
#
# Some hints:
# Could negative integers be palindromes? (ie, -1)
#
# If you are thinking of converting the integer to string, note the restriction of using extra space.
#
# You could also try reversing an integer. However, if you have solved the problem "Reverse Integer", you know that the reversed integer might overflow. How would you handle such case?
#
# There is a more generic way of solving this problem.

class Solution:
    def isPalindrome(self, x):
        """
        :type x: int
        :rtype: bool
        """
        if x < 0:
            return False
        if 0 <= x <= 9:
            return True
        length = 1
        while x % pow(10, length) != x:
            length += 1
        if length % 2 == 0:
            while length > 0:
                if (int)(x / pow(10, length - 1)) != x % 10:
                    return False
                x = (int)((x / 10) % pow(10, length - 2))
                length -= 2
            return True
        else:
            while length > 1:
                if (int)(x / pow(10, length - 1)) != x % 10:
                    return False
                x = (int)((x / 10) % pow(10, length - 2))
                length -= 2
            return True
