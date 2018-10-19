# Given a binary array, find the maximum number of consecutive 1s in this array if you can flip at most one 0.
#
# Example 1:
# Input: [1,0,1,1,0]
# Output: 4
# Explanation: Flip the first zero will get the the maximum number of consecutive 1s.
#     After flipping, the maximum number of consecutive 1s is 4.
# Note:
#
# The input array will only contain 0 and 1.
# The length of input array is a positive integer and will not exceed 10,000
# Follow up:
# What if the input numbers come in one by one as an infinite stream? In other words, you can't store all numbers coming from the stream as it's too large to hold in memory. Could you solve it efficiently?


class Solution:
    def findMaxConsecutiveOnes(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        # res, count, flip = 0, 0, 1
        # i, last = 0, 0
        # remember last 0 index
        # while i < len(nums):
        #     num = nums[i]
        #     if num == 1:
        #         count += 1
        #     else:
        #         if flip == 1:
        #             count += 1
        #             flip = 0
        #             last = i
        #         else:
        #             res = max(res, count)
        #             count = 0
        #             flip = 1
        #             i = last
        #     i += 1
        # res = max(res, count)
        # return res
        res = 0
        cur, last = 0, 0
        for num in nums:
            if num == 1:
                cur += 1
            else:
                res = max(res, cur + last + 1)
                last = cur
                cur = 0
        res = max(res, cur + last + 1)
        return res


s = Solution()
print(s.findMaxConsecutiveOnes([1, 0, 1, 1, 0, 1]))
