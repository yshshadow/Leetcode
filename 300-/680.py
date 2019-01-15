# Given a non-empty string s, you may delete at most one character. Judge whether you can make it a palindrome.
#
# Example 1:
# Input: "aba"
# Output: True
# Example 2:
# Input: "abca"
# Output: True
# Explanation: You could delete the character 'c'.
# Note:
# The string will only contain lowercase characters a-z. The maximum length of the string is 50000.

class Solution:
    def validPalindrome(self, s):
        """
        :type s: str
        :rtype: bool
        """
        def isPalindrome(i,j):
            return s[i:j+1] == s[i:j+1][::-1]
        if not s:
            return True
        i,j = 0,len(s)-1
        while i<j:
            if s[i] != s[j]:
                return isPalindrome(i+1,j) or isPalindrome(i,j-1)
            i+=1
            j-=1
        return True