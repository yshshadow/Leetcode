# Given a string s consists of upper/lower-case alphabets and empty space characters ' ', return the length of last word in the string.
#
# If the last word does not exist, return 0.
#
# Note: A word is defined as a character sequence consists of non-space characters only.
#
# Example:
#
# Input: "Hello World"
# Output: 5

class Solution:
    def lengthOfLastWord(self, s):
        """
        :type s: str
        :rtype: int
        """
        arr = s.split(" ")
        if len(arr) == 0:
            return 0
        else:
            for index in range(0, len(arr))[::-1]:
                if arr[index] != "":
                    return len(arr[index])
        return 0


s = Solution()
print(s.lengthOfLastWord("a "))
print(s.lengthOfLastWord("a"))
