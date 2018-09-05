# Write a function that takes a string as input and returns the string reversed.
#
# Example 1:
#
# Input: "hello"
# Output: "olleh"
# Example 2:
#
# Input: "A man, a plan, a canal: Panama"
# Output: "amanaP :lanac a ,nalp a ,nam A"

class Solution(object):
    def reverseString(self, s):
        """
        :type s: str
        :rtype: str
        """
        if not s or len(s) < 2:
            return s
        l = list(s)
        i, j = 0, len(l) - 1
        while i < j:
            temp = l[i]
            l[i] = l[j]
            l[j] = temp
            i += 1
            j -= 1
        return ''.join(l)
