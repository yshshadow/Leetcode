# Given a string, find the first non-repeating character in it and return it's index. If it doesn't exist, return -1.
#
# Examples:
#
# s = "leetcode"
# return 0.
#
# s = "loveleetcode",
# return 2.
# Note: You may assume the string contain only lowercase letters.
import collections
class Solution(object):
    def firstUniqChar(self, s):
        """
        :type s: str
        :rtype: int
        """
        # if not s or len(s) == 0:
        #     return -1
        # if len(s) == 1:
        #     return 0
        # dic = {}
        # for char in s:
        #     if char not in dic:
        #         dic[char] = 1
        #     else:
        #         dic[char] += 1
        # for idx in range(len(s)):
        #     if dic[s[idx]] == 1:
        #         return idx
        # return -1

        #use collections.Counter
        c = collections.Counter(s)
        for i, char in enumerate(s):
            if c[char] == 1:
                return i
        return -1
