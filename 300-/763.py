# A string S of lowercase letters is given. We want to partition this string into as many parts as possible so that each letter appears in at most one part, and return a list of integers representing the size of these parts.
#
# Example 1:
# Input: S = "ababcbacadefegdehijhklij"
# Output: [9,7,8]
# Explanation:
# The partition is "ababcbaca", "defegde", "hijhklij".
# This is a partition so that each letter appears in at most one part.
# A partition like "ababcbacadefegde", "hijhklij" is incorrect, because it splits S into less parts.
# Note:
#
# S will have length in range [1, 500].
# S will consist of lowercase letters ('a' to 'z') only.


class Solution(object):
    def partitionLabels(self, S):
        """
        :type S: str
        :rtype: List[int]
        """
        start, end, pos = 0, 1, 0
        dic = set()
        res = []
        while end <= len(S):
            while pos < end:
                if S[pos] in dic:
                    pos += 1
                    continue
                dic.add(S[pos])
                last = start
                for idx in range(start, len(S)):
                    if S[idx] == S[pos]:
                        last = idx
                end = max(end,last + 1)
            res.append(end-start)
            start, pos = end, end
            end += 1
        return res


s = Solution()
print(s.partitionLabels("ababcbacadefegdehijhklij"))
print(s.partitionLabels("eaaaabaaec"))
print(s.partitionLabels("andapnbpw"))
