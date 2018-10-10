# A
# matrix is Toeplitz if every
# diagonal
# from top
#
# -left
# to
# bottom - right
# has
# the
# same
# element.
#
# Now
# given
# an
# M
# x
# N
# matrix,
# return True if and only if the
# matrix is Toeplitz.
#
# Example
# 1:
#
# Input:
# matrix = [
#     [1, 2, 3, 4],
#     [5, 1, 2, 3],
#     [9, 5, 1, 2]
# ]
# Output: True
# Explanation:
# In
# the
# above
# grid, the
# diagonals
# are:
# "[9]", "[5, 5]", "[1, 1, 1]", "[2, 2, 2]", "[3, 3]", "[4]".
# In
# each
# diagonal
# all
# elements
# are
# the
# same, so
# the
# answer is True.
# Example
# 2:
#
# Input:
# matrix = [
#     [1, 2],
#     [2, 2]
# ]
# Output: False
# Explanation:
# The
# diagonal
# "[1, 2]"
# has
# different
# elements.
#
# Note:
#
# matrix
# will
# be
# a
# 2
# D
# array
# of
# integers.
# matrix
# will
# have
# a
# number
# of
# rows and columns in range[1, 20].
# matrix[i][j]
# will
# be
# integers in range[0, 99].
#
# Follow
# up:
#
# What if the
# matrix is stored
# on
# disk, and the
# memory is limited
# such
# that
# you
# can
# only
# load
# at
# most
# one
# row
# of
# the
# matrix
# into
# the
# memory
# at
# once?
# What if the
# matrix is so
# large
# that
# you
# can
# only
# load
# up
# a
# partial
# row
# into
# the
# memory
# at
# once?

class Solution(object):
    def isToeplitzMatrix(self, matrix):
        """
        :type matrix: List[List[int]]
        :rtype: bool
        """
        # compare to left-top way
        # lx, ly = len(matrix), len(matrix[0])
        # i, j = lx - 1, 0 # start at left-bottom
        # while 0 <= i < lx and 0 <= j < ly:
        #     num = matrix[i][j]
        #     x, y = i, j
        #     while 0 <= x < lx and 0 <= y < ly:
        #         if matrix[x][y] != num:
        #             return False
        #         x += 1
        #         y += 1
        #     if j == 0 and i == 0: # when i,j is 0, turn right
        #         j += 1
        #     elif i == 0:
        #         j += 1
        #     elif j == 0:
        #         i -= 1
        # return True

        # make groups
        group = {}
        for r in range(len(matrix)):
            for c in range(len(matrix[0])):
                if r - c not in group:
                    group[r - c] = matrix[r][c]
                elif group[r - c] != matrix[r][c]:
                    return False
        return True


s = Solution()
print(s.isToeplitzMatrix([[1, 2, 3, 4],
                          [5, 1, 2, 3],
                          [9, 5, 1, 2]]))
