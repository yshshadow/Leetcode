# Write a function to find the longest common prefix string amongst an array of strings.
#
# If there is no common prefix, return an empty string "".
#
# Example 1:
#
# Input: ["flower","flow","flight"]
# Output: "fl"
# Example 2:
#
# Input: ["dog","racecar","car"]
# Output: ""
# Explanation: There is no common prefix among the input strings.
# Note:
#
# All given inputs are in lowercase letters a-z.

class Solution(object):
    def longestCommonPrefix(self, strs):
        """
        :type strs: List[str]
        :rtype: str
        """
        if not strs or len(strs) == 0:
            return ''
        res = ''
        idx = 0
        while True:
            if idx < len(strs[0]):
                pre = strs[0][idx]
            else:
                return res
            for word in strs:
                if idx >= len(word) or word[idx] != pre:
                    return res
                else:
                    pre = word[idx]
            res += pre
            idx += 1
        return res


s = Solution()
print(s.longestCommonPrefix(["", "flower", "flow", "floght"]))
