# Given two strings S and T, return if they are equal when both are typed into empty text editors. # means a backspace character.
#
# Example 1:
#
# Input: S = "ab#c", T = "ad#c"
# Output: true
# Explanation: Both S and T become "ac".
# Example 2:
#
# Input: S = "ab##", T = "c#d#"
# Output: true
# Explanation: Both S and T become "".
# Example 3:
#
# Input: S = "a##c", T = "#a#c"
# Output: true
# Explanation: Both S and T become "c".
# Example 4:
#
# Input: S = "a#c", T = "b"
# Output: false
# Explanation: S becomes "c" while T becomes "b".
# Note:
#
# 1 <= S.length <= 200
# 1 <= T.length <= 200
# S and T only contain lowercase letters and '#' characters.
# Follow up:
#
# Can you solve it in O(N) time and O(1) space?
import itertools


class Solution(object):
    def backspaceCompare(self, S, T):
        """
        :type S: str
        :type T: str
        :rtype: bool
        """

        # O(N) time and O(N) space
        # sl, tl = [], []
        # for s in S:
        #     if s == '#':
        #         if len(sl) > 0:
        #             sl.pop()
        #     else:
        #         sl.append(s)
        # for t in T:
        #     if t == '#':
        #         if len(tl) > 0:
        #             tl.pop()
        #     else:
        #         tl.append(t)
        # return ''.join(sl) == ''.join(tl)

        # O(N) time and O(1) space use yield, not work on leetcode
        # def nextChar(S):
        #     skip = 0
        #     for s in reversed(S):
        #         if s == '#':
        #             skip += 1
        #         elif skip > 0:
        #             skip -= 1
        #         else:
        #             yield s
        #
        # return all(x == y for x, y in itertools.zip_longest(nextChar(S), nextChar(T)))

        # O(N) time and O(1) space use loop
        ls, lt = len(S), len(T)
        i, j = ls - 1, lt - 1
        while i >= 0 or j >= 0:  # lenS lenT is not equal, only can use or
            skip = 0  # must use skip instead of -2 directly, because # can appear more than once in same place
            while i >= 0:
                if S[i] == '#':
                    i -= 1
                    skip += 1
                elif skip:
                    skip -= 1
                    i -= 1
                else:
                    break
            while j >= 0:
                if T[j] == '#':
                    j -= 1
                    skip += 1
                elif skip:
                    skip -= 1
                    j -= 1
                else:
                    break
            if i >= 0 and j >= 0 and S[i] != T[j]:
                return False
            if (i >= 0) != (j >= 0):
                return False
            i -= 1
            j -= 1
        return True


s = Solution()
print(s.backspaceCompare("bbbextm",
                         "bbb#extm"))
