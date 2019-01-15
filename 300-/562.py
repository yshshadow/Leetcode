# Given a 01 matrix M, find the longest line of consecutive one in the matrix. The line could be horizontal, vertical, diagonal or anti-diagonal.
# Example:
# Input:
# [[0,1,1,0],
#  [0,1,1,0],
#  [0,0,0,1]]
# Output: 3
# Hint: The number of elements in the given matrix will not exceed 10,000.

class Solution(object):
    def longestLine(self, M):
        """
        :type M: List[List[int]]
        :rtype: int
        """
        dp = [[[0, 0, 0, 0] for _ in range(len(M[0]))] for _ in range(len(M))]
        for i in range(len(M)):
            for j in range(len(M[0])):
                if M[i][j] == 1:
                    dp[i][j] = [1, 1, 1, 1]
        for i in range(len(M)):
            for j in range(len(M[0])):
                if M[i][j] != 1:
                    continue
                if i == 0 and j == 0:
                    continue
                elif i == 0:
                    dp[i][j][0] += dp[i][j - 1][0] if M[i][j - 1] == 1 else 0
                elif j == 0:
                    dp[i][j][1] += dp[i - 1][j][1] if M[i - 1][j] == 1 else 0
                    if j + 1 < len(M[0]):
                        dp[i][j][3] += dp[i - 1][j + 1][3] if M[i - 1][j + 1] == 1 else 0
                elif j == len(M[0]) - 1:
                    dp[i][j][0] += dp[i][j - 1][0] if M[i][j - 1] == 1 else 0
                    dp[i][j][1] += dp[i - 1][j][1] if M[i - 1][j] == 1 else 0
                    if j - 1 >= 0:
                        dp[i][j][2] += dp[i - 1][j - 1][2] if M[i - 1][j - 1] == 1 else 0
                else:
                    dp[i][j][0] += dp[i][j - 1][0] if M[i][j - 1] == 1 else 0
                    dp[i][j][1] += dp[i - 1][j][1] if M[i - 1][j] == 1 else 0
                    dp[i][j][2] += dp[i - 1][j - 1][2] if M[i - 1][j - 1] == 1 else 0
                    dp[i][j][3] += dp[i - 1][j + 1][3] if M[i - 1][j + 1] == 1 else 0
        return self.getMax(dp)

    def getMax(self, dp):
        res = 0
        for i in range(len(dp)):
            for j in range(len(dp[0])):
                res = max(res, max(dp[i][j]))
        return res


s = Solution()
print(s.longestLine([[1, 1, 0, 0, 1, 0, 0, 1, 1, 0],
                     [1, 0, 0, 1, 0, 1, 1, 1, 1, 1],
                     [1, 1, 1, 0, 0, 1, 1, 1, 1, 0],
                     [0, 1, 1, 1, 0, 1, 1, 1, 1, 1],
                     [0, 0, 1, 1, 1, 1, 1, 1, 1, 0],
                     [1, 1, 1, 1, 1, 1, 0, 1, 1, 1],
                     [0, 1, 1, 1, 1, 1, 1, 0, 0, 1],
                     [1, 1, 1, 1, 1, 0, 0, 1, 1, 1],
                     [0, 1, 0, 1, 1, 0, 1, 1, 1, 1],
                     [1, 1, 1, 0, 1, 0, 1, 1, 1, 1]]))
