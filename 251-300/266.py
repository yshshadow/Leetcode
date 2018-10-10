# Given a string, determine if a permutation of the string could form a palindrome.
#
# Example 1:
#
# Input: "code"
# Output: false
# Example 2:
#
# Input: "aab"
# Output: true
# Example 3:
#
# Input: "carerac"
# Output: true
import collections


class Solution:
    def canPermutePalindrome(self, s):
        """
        :type s: str
        :rtype: bool
        """
        kv = collections.defaultdict(lambda: 0)
        for c in s:
            kv[c] += 1
        times = 0
        for v in kv.values():
            if v % 2 != 0:
                times += 1
        return times <= 1


