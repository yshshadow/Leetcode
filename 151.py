# Given an input string, reverse the string word by word.
#
# For example,
# Given s = "the sky is blue",
# return "blue is sky the".

class Solution(object):
    def reverseWords(self, s):
        """
        :type s: str
        :rtype: str
        """
        return " ".join(s.split()[::-1])
        # 交换法leetcode过不去case 删中间空格太折腾了
        #     if not s or len(s) == 0:
        #         return ""
        #     ls = list(s)
        #     self.reverse(ls, 0, len(s) - 1)
        #     idx, idy, length = 0, 0, len(s)
        #     while idx < length:
        #         while idy < length:
        #             if ls[idy] == ' ':
        #                 break
        #             idy += 1
        #         self.reverse(ls, idx, idy-1)
        #         idy += 1
        #         idx = idy
        #     return "".join(ls).strip().trim()
        #
        # def reverse(self, s, begin, end):
        #     while begin < end:
        #         temp = s[begin]
        #         s[begin] = s[end]
        #         s[end] = temp
        #         begin += 1
        #         end -= 1


st = "abc   edt "
print(st.strip())
s = Solution()
print(s.reverseWords(st))
