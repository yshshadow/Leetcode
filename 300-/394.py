# Given an encoded string, return it's decoded string.
#
# The encoding rule is: k[encoded_string], where the encoded_string inside the square brackets is being repeated exactly k times. Note that k is guaranteed to be a positive integer.
#
# You may assume that the input string is always valid; No extra white spaces, square brackets are well-formed, etc.
#
# Furthermore, you may assume that the original data does not contain any digits and that digits are only for those repeat numbers, k. For example, there won't be input like 3a or 2[4].
#
# Examples:
#
# s = "3[a]2[bc]", return "aaabcbc".
# s = "3[a2[c]]", return "accaccacc".
# s = "2[abc]3[cd]ef", return "abcabccdcdcdef".

import collections


class Solution(object):
    def decodeString(self, s):
        """
        :type s: str
        :rtype: str
        """
        nums = collections.deque()
        chars = collections.deque()
        res = ""
        num = ""
        for char in s:
            if ord('a') <= ord(char) <= ord('z') or ord('A') <= ord(char) <= ord('Z'):
                if len(chars) > 0 and chars[0] == '[':
                    chars.append(char)
                else:
                    res += char
            elif char == '[':
                chars.append(char)
                nums.append(int(num))
                num = ""
            elif char == ']':
                times = nums.pop()
                strs = ""
                while chars[-1] != '[':
                    strs = chars.pop() + strs
                chars.pop()
                if len(chars) != 0:
                    chars.append(times * strs)
                else:
                    res += times * strs
            elif ord('0') <= ord(char) <= ord('9'):
                num += char
        return res


s = Solution()
# print(s.decodeString("2[abc]3[cd]ef"))
# print(s.decodeString("3[a2[c]]"))
# print(s.decodeString("3[z]2[2[y]pq4[2[jk]e1[f]]]ef"))
print(s.decodeString("3[a]2[b4[F]c]"))
# print(ord('z')<ord('Z'))