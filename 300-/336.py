# Given a list of unique words, find all pairs of distinct indices (i, j) in the given list, so that the concatenation of the two words, i.e. words[i] + words[j] is a palindrome.
#
# Example 1:
#
# Input: ["abcd","dcba","lls","s","sssll"]
# Output: [[0,1],[1,0],[3,2],[2,4]]
# Explanation: The palindromes are ["dcbaabcd","abcddcba","slls","llssssll"]
# Example 2:
#
# Input: ["bat","tab","cat"]
# Output: [[0,1],[1,0]]
# Explanation: The palindromes are ["battab","tabbat"]

class Solution(object):
    def palindromePairs(self, words):
        """
        :type words: List[str]
        :rtype: List[List[int]]
        """
        res = []
        if not words:
            return res
        maps = {}
        for i, word in enumerate(words):
            maps[word] = i
        # '' can concatenate to any palindrome string
        if '' in maps:
            j = maps['']
            for i, word in enumerate(words):
                if i == j:
                    continue
                elif self.isPalindrome(word):
                    res.append([i, j])
                    res.append([j, i])
        # if reversed string in words
        for i, word in enumerate(words):
            reverse = word[::-1]
            if reverse in maps and maps[reverse] != i:
                j = maps[reverse]
                res.append([i, j])
                # only add one, the another one will be added after
                # res.append([j,i])
        # case1 : s1[0:cut] is palindrome and s1[cut+1:] = reverse(s2) => (s2, s1)
        # case2 : s1[cut+1:] is palindrome and s1[0:cut] = reverse(s2) => (s1, s2)
        for i, word in enumerate(words):
            for cut in range(1, len(word)):
                if self.isPalindrome(word[:cut]):
                    reverse = word[cut:][::-1]
                    if reverse in maps and maps[reverse] != i:
                        res.append([maps[reverse], i])
                if self.isPalindrome(word[cut:]):
                    reverse = word[:cut][::-1]
                    if reverse in maps and maps[reverse] != i:
                        res.append([i, maps[reverse]])
        return res

    def isPalindrome(self, s):
        return s == s[::-1]

s=Solution()
print(s.palindromePairs(["abcd","dcba","lls","s","sssll"]))