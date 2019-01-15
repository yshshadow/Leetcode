# Write a program to solve a Sudoku puzzle by filling the empty cells.
#
# A sudoku solution must satisfy all of the following rules:
#
# Each of the digits 1-9 must occur exactly once in each row.
# Each of the digits 1-9 must occur exactly once in each column.
# Each of the the digits 1-9 must occur exactly once in each of the 9 3x3 sub-boxes of the grid.
# Empty cells are indicated by the character '.'.
#
#
# A sudoku puzzle...
#
#
# ...and its solution numbers marked in red.
#
# Note:
#
# The given board contain only digits 1-9 and the character '.'.
# You may assume that the given Sudoku puzzle will have a single unique solution.
# The given board size is always 9x9.


import copy


class Solution:
    def __init__(self):
        self.board = None
        self.possible_board = None  # 可能性矩阵，存放每个格子可能的值
        self.empty_list = []  # [(i,j)]，存放空缺的位置

    def solveSudoku(self, board):
        """
        :type board: List[List[str]]
        :rtype: void Do not return anything, modify board in-place instead.
        回溯法。
        """

        # 初始化
        self.board = [['.' for x in range(9)] for y in range(9)]
        self.possible_board = [[set([str(y) for y in range(1, 10)]) for x in range(9)] for z in range(9)]
        self.empty_list = []
        for i in range(9):
            for j in range(9):
                if board[i][j] == '.':
                    self.empty_list.append((i, j))
                elif not self.set_value(i, j, board[i][j]):
                    return

        # 空缺位置排序，从可能性最少的位置开始
        self.empty_list = sorted(self.empty_list, key=lambda x: len(self.possible_board[x[0]][x[1]]))

        # 开始回溯
        self.backtrack(0)

        # 复制给board
        for i in range(9):
            for j in range(9):
                board[i][j] = self.board[i][j]

    def update_possible(self, i, j, ex_value):
        '''
        更新(i,j)位置的可能性，去除ex_value这个可能值
        '''
        # 已经是这个值了
        if self.board[i][j] == ex_value:
            return False

        # 本来就不可能是ex_value
        if ex_value not in self.possible_board[i][j]:
            return True

        # 去除可能值
        self.possible_board[i][j].remove(ex_value)

        # 可能性为空
        if not self.possible_board[i][j]:
            return False

        # 可能性为多个
        if len(self.possible_board[i][j]) > 1:
            return True

        # 只有一种可能性，直接赋值
        return self.set_value(i, j, list(self.possible_board[i][j])[0])

    def set_value(self, i, j, v):
        '''
        在(i,j)的位置上放入v
        '''

        # 本来就是v
        if self.board[i][j] == v:
            return True

        # 不可能是v
        if v not in self.possible_board[i][j]:
            return False

        # 赋值
        self.board[i][j] = v
        self.possible_board[i][j] = {v}

        # 修改同行、同列、同子块的其他位置的可能性
        for k in range(9):
            if k != i and not self.update_possible(k, j, v):
                return False
            if k != j and not self.update_possible(i, k, v):
                return False
            sub_i = i // 3 * 3 + k // 3
            sub_j = j // 3 * 3 + k % 3
            if sub_i != i and sub_j != j and not self.update_possible(sub_i, sub_j, v):
                return False
        return True

    def backtrack(self, k):
        '''
        为第k个之后的所有空缺位置填补数字
        '''
        if k >= len(self.empty_list):
            return True
        i = self.empty_list[k][0]
        j = self.empty_list[k][1]

        # 已经有数字，则跳过
        if self.board[i][j] != '.':
            return self.backtrack(k + 1)

        # 备份，便于回溯
        board_bak = copy.deepcopy(self.board)
        possible_board_bak = copy.deepcopy(self.possible_board)

        # 遍历所有可能的数字
        possible_list = list(self.possible_board[i][j])
        for v in possible_list:
            if self.set_value(i, j, v) and self.backtrack(k + 1):
                # 可以设置当前值，且之后所有空缺位置也可以填充值
                return True
            # 设置失败，回溯
            self.board = board_bak
            self.possible_board = possible_board_bak
        return False