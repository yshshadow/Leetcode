# Given a 2D board and a word, find if the word exists in the grid.
#
# The word can be constructed from letters of sequentially adjacent cell, where "adjacent" cells are those horizontally or vertically neighboring. The same letter cell may not be used more than once.
#
# Example:
#
# board =
# [
#   ['A','B','C','E'],
#   ['S','F','C','S'],
#   ['A','D','E','E']
# ]
#
# Given word = "ABCCED", return true.
# Given word = "SEE", return true.
# Given word = "ABCB", return false.

class Solution(object):
    def exist(self, board, word):
        """
        :type board: List[List[str]]
        :type word: str
        :rtype: bool
        """
        lx, ly = len(board), len(board[0])

        def dfs(word, x, y, visited):
            if len(word) == 0:
                return True
            elif (x, y) in visited:
                return False
            elif x < 0 or x >= lx or y < 0 or y >= ly:
                return False
            elif word[0] == board[x][y]:
                visited.add((x, y))
                re = any(
                    map(lambda x: dfs(word[1:], x[0], x[1], visited), [(x - 1, y), (x + 1, y), (x, y - 1), (x, y + 1)]))
                if not re: visited.remove((x, y))
                return re
            else:
                return False

        for i in range(lx):
            for j in range(ly):
                if dfs(word, i, j, set()):
                    return True
        return False


s = Solution()
print(s.exist([["A", "B", "C", "E"], ["S", "F", "E", "S"], ["A", "D", "E", "E"]],
              "ABCESEEEFS"))
