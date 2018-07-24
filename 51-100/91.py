# A message containing letters from A-Z is being encoded to numbers using the following mapping:
#
# 'A' -> 1
# 'B' -> 2
# ...
# 'Z' -> 26
# Given a non-empty string containing only digits, determine the total number of ways to decode it.
#
# Example 1:
#
# Input: "12"
# Output: 2
# Explanation: It could be decoded as "AB" (1 2) or "L" (12).
# Example 2:
#
# Input: "226"
# Output: 3
# Explanation: It could be decoded as "BZ" (2 26), "VF" (22 6), or "BBF" (2 2 6).

class Solution(object):
    def numDecodings(self, s):
        """
        :type s: str
        :rtype: int
        """
        if len(s) == 0 or s[0] == '0':
            return 0
        if len(s) == 1:
            return 1
        dp = [0] * len(s)
        dp[0] = 1
        if s[1] == '0':
            if '0' < s[0] < '3':
                dp[1] = 1
            else:
                return 0
        elif s[0] == '1' or (s[0] == '2' and s[1] < '7'):
            dp[1] = 2
        else:
            dp[1] = 1
        if len(s) == 2:
            return dp[1]
        for idx in range(2, len(s)):
            if s[idx] == '0':
                if s[idx - 1] == '0' or s[idx - 1] > '2':
                    return 0
                dp[idx] = dp[idx - 2]
            elif s[idx - 1] == '1' or (s[idx - 1] == '2' and s[idx] < '7'):
                dp[idx] = dp[idx - 1] + dp[idx - 2]
            else:
                dp[idx] = dp[idx - 1]
        return dp[len(s) - 1]


s = Solution()
print(s.numDecodings("226"))
