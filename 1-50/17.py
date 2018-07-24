# Given a string containing digits from 2-9 inclusive, return all possible letter combinations that the number could represent.
#
# A mapping of digit to letters (just like on the telephone buttons) is given below. Note that 1 does not map to any letters.
#
# Input: "23"
# Output: ["ad", "ae", "af", "bd", "be", "bf", "cd", "ce", "cf"].
# Note:
#
# Although the above answer is in lexicographical order, your answer could be in any order you want.

class Solution(object):
    dic = {"2": "abc", "3": "def", "4": "ghi", "5": "jkl", "6": "mno", "7": "pqrs", "8": "tuv", "9": "wxyz"}

    def letterCombinations(self, digits):
        """
        :type digits: str
        :rtype: List[str]
        """
        if digits == '':
            return []
        res = []
        self.dfs(digits, 0, res, '')
        return res

    def dfs(self, digits, level, res, path):
        if len(path) == len(digits):
            res.append(path)
            return
        for j in self.dic[digits[level]]:
            self.dfs(digits, level + 1, res, path + j)
            # for i in range(level, len(digits)):
            #     for j in self.dic[digits[i]]:
            #         self.dfs(digits, i + 1, res, path + j)


s = Solution()
print(s.letterCombinations("23"))
