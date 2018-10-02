# Compare two version numbers version1 and version2.
# If version1 > version2 return 1; if version1 < version2 return -1;otherwise return 0.
#
# You may assume that the version strings are non-empty and contain only digits and the . character.
# The . character does not represent a decimal point and is used to separate number sequences.
# For instance, 2.5 is not "two and a half" or "half way to version three", it is the fifth second-level revision of the second first-level revision.
#
# Example 1:
#
# Input: version1 = "0.1", version2 = "1.1"
# Output: -1
# Example 2:
#
# Input: version1 = "1.0.1", version2 = "1"
# Output: 1
# Example 3:
#
# Input: version1 = "7.5.2.4", version2 = "7.5.3"
# Output: -1

class Solution(object):
    def compareVersion(self, version1, version2):
        """
        :type version1: str
        :type version2: str
        :rtype: int
        """
        v1 = version1.split('.')
        v2 = version2.split('.')
        l = min(len(v1), len(v2))
        if l == len(v1):
            v1 += [0] * (len(v2) - l)
        else:
            v2 += [0] * (len(v1) - l)
        for i in range(len(v1)):
            c1, c2 = int(v1[i]), int(v2[i])
            if c1 > c2:
                return 1
            elif c1 < c2:
                return -1

        return 0


s = Solution()
s.compareVersion('1.1', '1')
