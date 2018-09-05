# Write a function that takes a string as input and reverse only the vowels of a string.
#
# Example 1:
#
# Input: "hello"
# Output: "holle"
# Example 2:
#
# Input: "leetcode"
# Output: "leotcede"
# Note:
# The vowels does not include the letter "y".

class Solution(object):
    def reverseVowels(self, s):
        """
        :type s: str
        :rtype: str
        """
        if not s or len(s) < 2:
            return s
        l = list(s)
        length = len(l)
        vowels = set(['a', 'e', 'i', 'o', 'u', 'A', 'E', 'I', 'O', 'U'])
        i, j = 0, length - 1
        while i < j:
            if l[i] not in vowels:
                i += 1
                continue
            if l[j] not in vowels:
                j -= 1
                continue
            if i < j:
                self.swap(l, i, j)
                i += 1
                j -= 1
        return ''.join(l)

    def swap(self, l, i, j):
        temp = l[i]
        l[i] = l[j]
        l[j] = temp


s = Solution()
print(s.reverseVowels("leetcode"))
