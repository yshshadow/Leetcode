# Given a string s, partition s such that every substring of the partition is a palindrome.
#
# Return the minimum cuts needed for a palindrome partitioning of s.
#
# Example:
#
# Input: "aab"
# Output: 1
# Explanation: The palindrome partitioning ["aa","b"] could be produced using 1 cut.

class Solution(object):
    def minCut(self, s):
        """
        :type s: str
        :rtype: int
        """
        m = [len(s) for _ in range(len(s))]
        p = [[False for _ in range(len(s))] for _ in range(len(s))]
        m[0] = 0

        def palindrome(s):
            return s == s[::-1]

        for i in range(len(s)):
            for j in range(i, len(s)):
                if palindrome(s[i:j + 1]):
                    p[i][j] = True

        for i in range(1, len(s)):
            if p[0][i]:
                m[i] = 0
                continue
            for j in range(1, i + 1):
                if p[j][i]:
                    m[i] = min(m[i], m[j-1] + 1)
        return m[-1]


s = Solution()
print(s.minCut('aab'))
print(s.minCut('abbacca'))
