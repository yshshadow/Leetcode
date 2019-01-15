# Given a string s1, we may represent it as a binary tree by partitioning it to two non-empty substrings recursively.
#
# Below is one possible representation of s1 = "great":
#
#     great
#    /    \
#   gr    eat
#  / \    /  \
# g   r  e   at
#            / \
#           a   t
# To scramble the string, we may choose any non-leaf node and swap its two children.
#
# For example, if we choose the node "gr" and swap its two children, it produces a scrambled string "rgeat".
#
#     rgeat
#    /    \
#   rg    eat
#  / \    /  \
# r   g  e   at
#            / \
#           a   t
# We say that "rgeat" is a scrambled string of "great".
#
# Similarly, if we continue to swap the children of nodes "eat" and "at", it produces a scrambled string "rgtae".
#
#     rgtae
#    /    \
#   rg    tae
#  / \    /  \
# r   g  ta  e
#        / \
#       t   a
# We say that "rgtae" is a scrambled string of "great".
#
# Given two strings s1 and s2 of the same length, determine if s2 is a scrambled string of s1.
#
# Example 1:
#
# Input: s1 = "great", s2 = "rgeat"
# Output: true
# Example 2:
#
# Input: s1 = "abcde", s2 = "caebd"
# Output: false
import collections


class Solution(object):
    def __init__(self):
        self.cache = set()

    def isScramble(self, s1, s2):
        """
        :type s1: str
        :type s2: str
        :rtype: bool
        """
        # if s1 s2 are scramble, s1[:i] and s2[:i] are scramble and s1[i:] and s2[i:] are scramble
        # or s1[:i] and s2[len-i:] are scramble and s1[len-i:] and s2[:i] are scramble
        if len(s1) != len(s2):
            return False
        if s1 == s2 or (s1, s2) in self.cache or (s2, s1) in self.cache:
            return True
        if collections.Counter(s1) != collections.Counter(s2):
            return False
        for i in range(1, len(s1)):
            if (self.isScramble(s1[:i], s2[:i]) and self.isScramble(s1[i:], s2[i:])) or \
                    (self.isScramble(s1[:i], s2[len(s2) - i:]) and self.isScramble(s1[i:], s2[:len(s2) - i])):
                self.cache.add((s1, s2))
                return True
        return False


s = Solution()
print(s.isScramble('great', 'rgeat'))
