# Given a string containing just the characters '(', ')', '{', '}', '[' and ']', determine if the input string is valid.
#
# The brackets must close in the correct order, "()" and "()[]{}" are all valid but "(]" and "([)]" are not.

class Solution:
    def isValid(self, s):
        """
        :type s: str
        :rtype: bool
        """
        stack = []
        for char in s:
            if char == '(' or char == '{' or char == '[':
                stack.append(char)
            else:
                if len(stack) == 0:
                    return False
                top = stack.pop()
                if top == '(' and char != ')':
                    return False
                if top == '{' and char != '}':
                    return False
                if top == '[' and char != ']':
                    return False
        if len(stack) > 0:
            return False
        return True


s = Solution()
print(s.isValid("[]"))