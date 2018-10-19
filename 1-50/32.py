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
        dp = [0 for _ in range(len(s))]
        for i in range(1, len(s)):
            if s[i] == ')' and s[i - 1] == '(':
                dp[i] = (dp[i - 2] if i >= 2 else 0) + 2
            elif s[i] == ')' and i - dp[i - 1] - 1 >= 0 and s[i - dp[i - 1] - 1] == '(':
                dp[i] = dp[i - 1] + (dp[i - dp[i - 1] - 2] if i - dp[i - 1] >= 2 else 0) + 2

        return max(dp)


s = Solution()
print(s.longestValidParentheses("(()())"))
