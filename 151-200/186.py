# Given an input string , reverse the string word by word.
#
# Example:
#
# Input:  ["t","h","e"," ","s","k","y"," ","i","s"," ","b","l","u","e"]
# Output: ["b","l","u","e"," ","i","s"," ","s","k","y"," ","t","h","e"]
# Note:
#
# A word is defined as a sequence of non-space characters.
# The input string does not contain leading or trailing spaces.
# The words are always separated by a single space.
# Follow up: Could you do it in-place without allocating extra space?

class Solution(object):
    def reverseWords(self, str):
        """
        :type str: List[str]
        :rtype: void Do not return anything, modify str in-place instead.
        """
        if not str:
            return
        i, j = 0, len(str) - 1
        while i < j:
            str[i], str[j] = str[j], str[i]
            i += 1
            j -= 1
        i, j = 0, 0
        while i < len(str):
            j = i
            while j < len(str):
                if str[j] == ' ':
                    break
                j += 1

            def reverse(str, i, j):
                j -= 1
                while i < j:
                    str[i], str[j] = str[j], str[i]
                    i += 1
                    j -= 1

            reverse(str, i, j)
            i = j + 1


s = Solution()
s.reverseWords(["t", "h", "e", " ", "s", "k", "y", " ", "i", "s", " ", "b", "l", "u", "e"])
