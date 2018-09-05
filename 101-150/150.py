# Evaluate the value of an arithmetic expression in Reverse Polish Notation.
#
# Valid operators are +, -, *, /. Each operand may be an integer or another expression.
#
# Note:
#
# Division between two integers should truncate toward zero.
# The given RPN expression is always valid. That means the expression would always evaluate to a result and there won't be any divide by zero operation.
# Example 1:
#
# Input: ["2", "1", "+", "3", "*"]
# Output: 9
# Explanation: ((2 + 1) * 3) = 9
# Example 2:
#
# Input: ["4", "13", "5", "/", "+"]
# Output: 6
# Explanation: (4 + (13 / 5)) = 6
# Example 3:
#
# Input: ["10", "6", "9", "3", "+", "-11", "*", "/", "*", "17", "+", "5", "+"]
# Output: 22
# Explanation:
#   ((10 * (6 / ((9 + 3) * -11))) + 17) + 5
# = ((10 * (6 / (12 * -11))) + 17) + 5
# = ((10 * (6 / -132)) + 17) + 5
# = ((10 * 0) + 17) + 5
# = (0 + 17) + 5
# = 17 + 5
# = 22

class Solution(object):
    def evalRPN(self, tokens):
        """
        :type tokens: List[str]
        :rtype: int
        """
        numstack = []
        for token in tokens:
            if token.isdigit() or (token[0] == '-' and len(token) > 1):
                numstack.append(int(token))
            else:
                num1, num2 = numstack.pop(), numstack.pop()
                if token == '+':
                    res = num2 + num1
                elif token == '-':
                    res = num2 - num1
                elif token == '*':
                    res = num2 * num1
                elif token == '/':
                    res = int(num2 / num1)
                    # res = int(float(num2) / float(num1)) #本机mac上跑可以，leetcode上要换成注释里的语句
                numstack.append(res)
        return numstack.pop()


# print('-11'.isdecimal())
# print('-11'.isdigit())
# print('-11'.isnumeric())
s = Solution()
print(s.evalRPN(["10","6","9","3","+","-11","*","/","*","17","+","5","+"]))