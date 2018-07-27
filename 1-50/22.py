# Given n pairs of parentheses, write a function to generate all combinations of well-formed parentheses.
#
# For example, given n = 3, a solution set is:
#
# [
#   "((()))",
#   "(()())",
#   "(())()",
#   "()(())",
#   "()()()"
# ]

class Solution(object):
    def generateParenthesis(self, n):
        """
        :type n: int
        :rtype: List[str]
        """
        if n == 0:
            return []
        res = []

        # pairs must have n left and n right
        def generate(s='', left=0, right=0):
            if len(s) == 2 * n:  # string length equal to 2n, add it to result
                res.append(s)
            if left < n:  # left parenthesis not equal to n, can add left
                generate(s + '(', left + 1, right)
            if right < left:  # right is less than left, can add right
                generate(s + ')', left, right + 1)

        generate()
        return res
