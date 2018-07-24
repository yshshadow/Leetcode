# Given a list of non negative integers, arrange them such that they form the largest number.
#
# For example, given [3, 30, 34, 5, 9], the largest formed number is 9534330.
#
# Note: The result may be very large, so you need to return a string instead of an integer.

class Solution:
    # @param {integer[]} nums
    # @return {string}
    def largestNumber(self, nums):
        n = [str(num) for num in nums]
        n.sort(key = LargerNumKey)
        # largest_num = ''.join(sorted(map(str, nums), key=LargerNumKey))
        return '0' if n[0] == '0' else ''.join(n)


class LargerNumKey(str):
    def __lt__(x, y):
        return x + y > y + x


def cmp(x, y):
    return x + y > y + x


s = Solution()
print(s.largestNumber([3, 30, 34, 5, 9]))
