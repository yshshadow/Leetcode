# Given a string containing just the characters '(' and ')', find the length of the longest valid (well-formed) parentheses substring.
#
# Example 1:
#
# Input: "(()"
# Output: 2
# Explanation: The longest valid parentheses substring is "()"
# Example 2:
#
# Input: ")()())"
# Output: 4
# Explanation: The longest valid parentheses substring is "()()"

class Solution(object):
    def longestValidParentheses(self, s):
        """
        :type s: str
        :rtype: int
        """
        # initialize
        dp = [[0] * len(s) for _ in range(len(s))]
        res = 0
        for length in range(2, len(s) + 1):
            for idx in range(len(s) - length + 1):
                if s[idx - 1] == '(':
                    dp[length - 1][idx] = dp[length - 1][idx - 2] + 2
                    res = max(res, length)
        return res


s = Solution()
print(s.longestValidParentheses("((()())"))
