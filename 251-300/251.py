# Implement an iterator to flatten a 2d vector.
#
# Example:
#
# Input: 2d vector =
# [
#   [1,2],
#   [3],
#   [4,5,6]
# ]
# Output: [1,2,3,4,5,6]
# Explanation: By calling next repeatedly until hasNext returns false,
#              the order of elements returned by next should be: [1,2,3,4,5,6].
# Follow up:
# As an added challenge, try to code it using only iterators in C++ or iterators in Java.

import collections


class Vector2D(object):
    def __init__(self, vec2d):
        """
        Initialize your data structure here.
        :type vec2d: List[List[int]]
        """

        def flatten(vec):
            for element in vec:
                if isinstance(element, list):
                    for e in element:
                        yield e
                else:
                    yield element

        self.vec = collections.deque(list(flatten(vec2d)))

    def next(self):
        """
        :rtype: int
        """
        return self.vec.popleft()

    def hasNext(self):
        """
        :rtype: bool
        """
        return len(self.vec) > 0


        # Your Vector2D object will be instantiated and called as such:
        # i, v = Vector2D(vec2d), []
        # while i.hasNext(): v.append(i.next())


s = Vector2D([
  [1,2],
  [3],
  [4,5,6]
])

