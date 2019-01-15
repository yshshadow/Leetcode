# Given a string S and a string T, find the minimum window in S which will contain all the characters in T in complexity O(n).
#
# Example:
#
# Input: S = "ADOBECODEBANC", T = "ABC"
# Output: "BANC"
# Note:
#
# If there is no such window in S that covers all characters in T, return the empty string "".
# If there is such window, you are guaranteed that there will always be only one unique minimum window in S.

import collections


class Solution(object):
    def minWindow(self, s, t):
        """
        :type s: str
        :type t: str
        :rtype: str
        """
        counter = collections.Counter(t)
        exist = collections.defaultdict(lambda: 0)
        for c in t:
            exist[c] = 0

        def check():
            for k in exist.keys():
                if exist[k] < counter[k]:
                    return False
            return True

        i, j = 0, 0
        res = ''
        while i <= j <= len(s):
            if check():
                res = s[i:j] if res == '' or len(res) > j - i else res
                if s[i] in exist:
                    exist[s[i]] -= 1
                i += 1
            else:
                if j < len(s) and s[j] in exist:
                    exist[s[j]] += 1
                j += 1
        return res


s = Solution()
print(s.minWindow("ADOBECODEBANC", "ABC"))
