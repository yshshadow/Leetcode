# Implement strStr().
#
# Return the index of the first occurrence of needle in haystack, or -1 if needle is not part of haystack.
#
# Example 1:
#
# Input: haystack = "hello", needle = "ll"
# Output: 2
# Example 2:
#
# Input: haystack = "aaaaa", needle = "bba"
# Output: -1
# Clarification:
#
# What should we return when needle is an empty string? This is a great question to ask during an interview.
#
# For the purpose of this problem, we will return 0 when needle is an empty string. This is consistent to C's strstr() and Java's indexOf().


class Solution(object):
    def strStr(self, haystack, needle):
        """
        :type haystack: str
        :type needle: str
        :rtype: int
        """
        # brute force TLE
        # if not haystack or not needle:
        #     return -1
        # for i in range(0, len(haystack) - len(needle)):
        #     for j in range(0, len(needle)):
        #         if needle[j] == haystack[i + j] and j == len(needle) - 1:
        #             return i
        #         if needle[j] != haystack[i + j]:
        #             break
        # return -1

        # KMP
        if not haystack:
            return -1
        if not needle:
            return 0
        nex = self.getNext(needle)
        i, j = 0, 0
        while i < len(haystack) and j < len(needle):
            if j == -1 or needle[j] == haystack[i]:
                j += 1
                i += 1
            else:
                j = nex[j]
        if j == len(needle):
            return i - j
        else:
            return -1

    def getNext(self, needle):
        nex = [0] * len(needle)
        nex[0] = -1
        i, j = 0, -1
        while i < len(needle) - 1:
            if j == -1 or needle[i] == needle[j]:
                j += 1
                i += 1
                nex[i] = j
            else:
                j = nex[j]
        return nex


s = Solution()
print(s.strStr("BBC ABCDAB ABCDABCDABDE",
               ""))
