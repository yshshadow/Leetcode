# Design a stack that supports push, pop, top, and retrieving the minimum element in constant time.
#
# push(x) -- Push element x onto stack.
# pop() -- Removes the element on top of the stack.
# top() -- Get the top element.
# getMin() -- Retrieve the minimum element in the stack.
# Example:
# MinStack minStack = new MinStack();
# minStack.push(-2);
# minStack.push(0);
# minStack.push(-3);
# minStack.getMin();   --> Returns -3.
# minStack.pop();
# minStack.top();      --> Returns 0.
# minStack.getMin();   --> Returns -2.


class MinStack(object):
    def __init__(self):
        """
        initialize your data structure here.
        """
        self.stack = []

    def push(self, x):
        """
        :type x: int
        :rtype: void
        """
        if len(self.stack):
            self.stack.append((x, x))
        else:
            v, mv = self.stack[-1]
            mv = min(mv, x)
            self.stack.append((x, mv))

    def pop(self):
        """
        :rtype: void
        """
        res,mv = self.stack.pop()
        return res

    def top(self):
        """
        :rtype: int
        """
        res = self.stack[-1]
        return res

    def getMin(self):
        """
        :rtype: int
        """
        v, mv = self.stack[-1]
        return mv



        # Your MinStack object will be instantiated and called as such:
        # obj = MinStack()
        # obj.push(x)
        # obj.pop()
        # param_3 = obj.top()
        # param_4 = obj.getMin()
