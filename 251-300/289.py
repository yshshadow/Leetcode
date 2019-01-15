# According to the Wikipedia's article: "The Game of Life, also known simply as Life, is a cellular automaton devised by the British mathematician John Horton Conway in 1970."
#
# Given a board with m by n cells, each cell has an initial state live (1) or dead (0). Each cell interacts with its eight neighbors (horizontal, vertical, diagonal) using the following four rules (taken from the above Wikipedia article):
#
# Any live cell with fewer than two live neighbors dies, as if caused by under-population.
# Any live cell with two or three live neighbors lives on to the next generation.
# Any live cell with more than three live neighbors dies, as if by over-population..
# Any dead cell with exactly three live neighbors becomes a live cell, as if by reproduction.
# Write a function to compute the next state (after one update) of the board given its current state. The next state is created by applying the above rules simultaneously to every cell in the current state, where births and deaths occur simultaneously.
#
# Example:
#
# Input:
# [
#   [0,1,0],
#   [0,0,1],
#   [1,1,1],
#   [0,0,0]
# ]
# Output:
# [
#   [0,0,0],
#   [1,0,1],
#   [0,1,1],
#   [0,1,0]
# ]
# Follow up:
#
# Could you solve it in-place? Remember that the board needs to be updated at the same time: You cannot update some cells first and then use their updated values to update other cells.
# In this question, we represent the board using a 2D array. In principle, the board is infinite, which would cause problems when the active area encroaches the border of the array. How would you address these problems?


class Solution:
    def getNeighborIndex(self, m, n, i, j):
        idx1 = [i - 1, i - 1, i - 1, i, i, i + 1, i + 1, i + 1]
        idx2 = [j - 1, j, j + 1, j - 1, j + 1, j - 1, j, j + 1]
        idx1_new = [x for i, x in enumerate(idx1) if 0 <= x < m and 0 <= idx2[i] < n]
        idx2_new = [x for i, x in enumerate(idx2) if 0 <= idx1[i] < m and 0 <= x < n]
        return idx1_new, idx2_new

    def countLiveCells(self, board, m, n, i, j):
        idx1, idx2 = self.getNeighborIndex(m, n, i, j)
        count = 0
        for t in range(len(idx1)):
            if board[idx1[t]][idx2[t]] == 1 or board[idx1[t]][idx2[t]] == -1:
                count += 1
        return count

    def gameOfLife(self, board):
        """
        :type board: List[List[int]]
        :rtype: void Do not return anything, modify board in-place instead.
        """
        # 活细胞如果有变化就标为-1， 死细胞如果有变化就标为-2，检查状态时要把这些考虑1和-1，最后再把-1和-2改回去
        m, n = len(board), len(board[0])
        if m < 1 or n < 1:
            return

        for i in range(m):
            for j in range(n):
                count = self.countLiveCells(board, m, n, i, j)
                if board[i][j] == 1 and (count < 2 or count > 3):
                    board[i][j] = -1
                elif board[i][j] == 0 and count == 3:
                    board[i][j] = -2

        for i in range(m):
            for j in range(n):
                if board[i][j] == -2:
                    board[i][j] = 1
                elif board[i][j] == -1:
                    board[i][j] = 0