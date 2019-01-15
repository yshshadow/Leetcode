# Given
# a
# 2
# D
# board
# containing
# 'X' and 'O'(the
# letter
# O), capture
# all
# regions
# surrounded
# by
# 'X'.
#
# A
# region is captured
# by
# flipping
# all
# 'O'
# s
# into
# 'X'
# s in that
# surrounded
# region.
#
# Example:
#
# X
# X
# X
# X
# X
# O
# O
# X
# X
# X
# O
# X
# X
# O
# X
# X
# After
# running
# your
# function, the
# board
# should
# be:
#
# X
# X
# X
# X
# X
# X
# X
# X
# X
# X
# X
# X
# X
# O
# X
# X
# Explanation:


# Surrounded regions shouldn’t be on the border, which means that any 'O' on the border of the board are not flipped to 'X'. Any 'O' that is not on the border and it is not connected to an 'O' on the border will be flipped to 'X'. Two cells are connected if they are adjacent cells connected horizontally or vertically.

class Solution(object):
    def solve(self, board):
        """
        :type board: List[List[str]]
        :rtype: void Do not return anything, modify board in-place instead.
        """
        visited = set()

        def dfs(i, j):
            if i < 0 or i >= len(board) or j < 0 or j >= len(board[0]):
                return
            if (i, j) in visited or board[i][j] != 'O':
                return
            visited.add((i, j))
            dfs(i - 1, j)
            dfs(i + 1, j)
            dfs(i, j - 1)
            dfs(i, j + 1)

        for i in range(len(board)):
            for j in (0, len(board[0]) - 1):
                if board[i][j] == 'O' and (i, j) not in visited:
                    dfs(i, j)
        for i in (0, len(board) - 1):
            for j in range(len(board[0])):
                if board[i][j] == 'O' and (i, j) not in visited:
                    dfs(i, j)
        for i in range(len(board)):
            for j in range(len(board[0])):
                if (i, j) not in visited:
                    board[i][j] = 'X'


s = Solution()
s.solve([["X", "X", "X", "X"], ["X", "O", "O", "X"], ["X", "X", "O", "X"], ["X", "O", "X", "X"]])
