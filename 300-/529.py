# Let's play the minesweeper game (Wikipedia, online game)!
#
# You are given a 2D char matrix representing the game board. 'M' represents an unrevealed mine, 'E' represents an unrevealed empty square, 'B' represents a revealed blank square that has no adjacent (above, below, left, right, and all 4 diagonals) mines, digit ('1' to '8') represents how many mines are adjacent to this revealed square, and finally 'X' represents a revealed mine.
#
# Now given the next click position (row and column indices) among all the unrevealed squares ('M' or 'E'), return the board after revealing this position according to the following rules:
#
# If a mine ('M') is revealed, then the game is over - change it to 'X'.
# If an empty square ('E') with no adjacent mines is revealed, then change it to revealed blank ('B') and all of its adjacent unrevealed squares should be revealed recursively.
# If an empty square ('E') with at least one adjacent mine is revealed, then change it to a digit ('1' to '8') representing the number of adjacent mines.
# Return the board when no more squares will be revealed.
# Example 1:
# Input:
#
# [['E', 'E', 'E', 'E', 'E'],
#  ['E', 'E', 'M', 'E', 'E'],
#  ['E', 'E', 'E', 'E', 'E'],
#  ['E', 'E', 'E', 'E', 'E']]
#
# Click : [3,0]
#
# Output:
#
# [['B', '1', 'E', '1', 'B'],
#  ['B', '1', 'M', '1', 'B'],
#  ['B', '1', '1', '1', 'B'],
#  ['B', 'B', 'B', 'B', 'B']]
#
# Explanation:
#
# Example 2:
# Input:
#
# [['B', '1', 'E', '1', 'B'],
#  ['B', '1', 'M', '1', 'B'],
#  ['B', '1', '1', '1', 'B'],
#  ['B', 'B', 'B', 'B', 'B']]
#
# Click : [1,2]
#
# Output:
#
# [['B', '1', 'E', '1', 'B'],
#  ['B', '1', 'X', '1', 'B'],
#  ['B', '1', '1', '1', 'B'],
#  ['B', 'B', 'B', 'B', 'B']]
#
# Explanation:
#
# Note:
# The range of the input matrix's height and width is [1,50].
# The click position will only be an unrevealed square ('M' or 'E'), which also means the input board contains at least one clickable square.
# The input board won't be a stage when game is over (some mines have been revealed).
# For simplicity, not mentioned rules should be ignored in this problem. For example, you don't need to reveal all the unrevealed mines when the game is over, consider any cases that you will win the game or flag any squares.


class Solution:
    def updateBoard(self, board, click):
        """
        :type board: List[List[str]]
        :type click: List[int]
        :rtype: List[List[str]]
        """
        x, y = click[0], click[1]
        self.updateNode(board, x, y)
        return board

    def updateNode(self, board, x, y):
        lx, ly = len(board), len(board[0])
        node = board[x][y]
        # click a mine
        if node == 'M':
            board[x][y] = 'X'
        elif node == 'E':
            # check neighbors
            count = 0
            for i, j in [(x - 1, y - 1), (x - 1, y), (x - 1, y + 1), (x, y - 1), (x, y + 1), (x + 1, y - 1), (x + 1, y),
                         (x + 1, y + 1)]:
                if 0 <= i < lx and 0 <= j < ly:
                    if board[i][j] == 'X' or board[i][j] == 'M':
                        count += 1
            if count > 0:
                board[x][y] = str(count)
            else:
                board[x][y] = 'B'
                for i, j in [(x - 1, y - 1), (x - 1, y), (x - 1, y + 1), (x, y - 1), (x, y + 1), (x + 1, y - 1),
                             (x + 1, y),
                             (x + 1, y + 1)]:
                    if 0 <= i < lx and 0 <= j < ly and board[i][j] == 'E':
                        self.updateNode(board, i, j)


s = Solution()
print(s.updateBoard([['E', 'E', 'E', 'E', 'E'],
                     ['E', 'E', 'M', 'E', 'E'],
                     ['E', 'E', 'E', 'E', 'E'],
                     ['E', 'E', 'E', 'E', 'E']], [3, 0]))
