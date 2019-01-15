# Given
# a
# string
# S,
# return the
# "reversed"
# string
# where
# all
# characters
# that
# are
# not a
# letter
# stay in the
# same
# place, and all
# letters
# reverse
# their
# positions.
#
# Example
# 1:
#
# Input: "ab-cd"
# Output: "dc-ba"
# Example
# 2:
#
# Input: "a-bC-dEf-ghIj"
# Output: "j-Ih-gfE-dCba"
# Example
# 3:
#
# Input: "Test1ng-Leet=code-Q!"
# Output: "Qedo1ct-eeLg=ntse-T!"
#
# Note:
#
# S.length <= 100
# 33 <= S[i].ASCIIcode <= 122
# S
# doesn
# 't contain \ or "

class Solution:
    def reverseOnlyLetters(self, S):
        """
        :type S: str
        :rtype: str
        """
        S = list(S)
        cset = set(list('abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUWVWXYZ'))
        i, j = 0, len(S) - 1
        while i < j:
            while i < j and S[i] not in cset:
                i += 1
            while i < j and S[j] not in cset:
                j -= 1
            S[i], S[j] = S[j], S[i]
            i += 1
            j -= 1
        return ''.join(S)


s = Solution()
print(s.reverseOnlyLetters("ab-cd"))
