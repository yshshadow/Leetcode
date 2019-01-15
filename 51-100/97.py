# Given s1, s2, s3, find whether s3 is formed by the interleaving of s1 and s2.
#
# Example 1:
#
# Input: s1 = "aabcc", s2 = "dbbca", s3 = "aadbbcbcac"
# Output: true
# Example 2:
#
# Input: s1 = "aabcc", s2 = "dbbca", s3 = "aadbbbaccc"
# Output: false

class Solution:
    def isInterleave(self, s1, s2, s3):
        """
        :type s1: str
        :type s2: str
        :type s3: str
        :rtype: bool
        """
        if len(s3) < len(s1) + len(s2):
            return False
        m = [[False for _ in range(len(s2) + 1)] for _ in range(len(s1) + 1)]
        m[1][0] = s3[0] == s1[0]
        m[0][1] = s3[0] == s2[0]
        m[0][0] = True
        for i in range(len(s1) + 1):
            for j in range(len(s2) + 1):
                if i == 0 and j == 0:
                    continue
                elif i == 0:
                    m[i][j] = s3[i + j - 1] == s2[j - 1] and m[i][j - 1]
                elif j == 0:
                    m[i][j] = s3[i + j - 1] == s1[i - 1] and m[i - 1][j]
                else:
                    m[i][j] = (s3[i + j - 1] == s1[i - 1] and m[i - 1][j]) or (
                        s3[i + j - 1] == s2[j - 1] and m[i][j - 1])
        return m[-1][-1]


s = Solution()
print(s.isInterleave("aabcc",
                     "dbbca",
                     "aadbbcbcac"))
