# Given an arbitrary ransom note string and another string containing letters from all the magazines, write a function that will return true if the ransom note can be constructed from the magazines ; otherwise, it will return false.
#
# Each letter in the magazine string can only be used once in your ransom note.
#
# Note:
# You may assume that both strings contain only lowercase letters.
#
# canConstruct("a", "b") -> false
# canConstruct("aa", "ab") -> false
# canConstruct("aa", "aab") -> true
import collections


class Solution(object):
    def canConstruct(self, ransomNote, magazine):
        """
        :type ransomNote: str
        :type magazine: str
        :rtype: bool
        """
        # return not collections.Counter(ransomNote) - collections.Counter(magazine)
        m_dict = collections.Counter(magazine)
        r_dict = collections.Counter(ransomNote)
        for k, v in r_dict.items():
            if m_dict[k] < v:
                return False
        return True
