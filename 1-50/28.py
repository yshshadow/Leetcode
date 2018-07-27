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
        # if needle == '':
        #     return 0
        # if haystack == '':
        #     return -1
        # res = -1
        # for idx, char in enumerate(haystack):
        #     if needle[0] == char:
        #         res = idx
        #         for idy in range(1, len(needle)):
        #             if idx + idy < len(haystack) and needle[idy] != haystack[idx + idy]:
        #                 res = -1
        #                 break
        #             elif idx + idy >= len(haystack):
        #                 res = -1
        #                 break
        #         if res != -1:
        #             return res
        # return res

        # KMP
        lengthOfHaystack = len(haystack)
        lengthOfNeedle = len(needle)
        if lengthOfNeedle == 0:
            return 0
        if lengthOfNeedle > lengthOfHaystack:
            return -1

        def getNext(needle):
            length = len(needle)
            nex = [0] * length
            nex[0] = -1
            j = -1
            for idx in range(length):
                if j == -1 or needle[idx] == needle[j]:
                    nex[idx] = j
                    j += 1
                else:
                    j = nex[j]
            return nex

        nex = getNext(needle)
        j = -1
        for i, char in enumerate(haystack):
            while j >= 0 and char != needle[j + 1]:
                j = nex[j]
            if char == needle[j + 1]:
                j += 1
            if j == lengthOfNeedle - 1:
                return i - lengthOfNeedle + 1
        return -1


s = Solution()
print(s.strStr("mississippi",
               "issi"))
