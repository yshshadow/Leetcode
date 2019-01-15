# Given a non-empty array of integers, every element appears three times except for one, which appears exactly once. Find that single one.
#
# Note:
#
# Your algorithm should have a linear runtime complexity. Could you implement it without using extra memory?
#
# Example 1:
#
# Input: [2,2,3,2]
# Output: 3
# Example 2:
#
# Input: [0,1,0,1,0,1,99]
# Output: 99

class Solution:
    def singleNumber(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        # counter = collections.Counter(nums)
        # for num in counter:
        #     if counter[num] == 1:
        #         return num
        # return 0

        # bit operation
        # count 1 on every bits, if it cannot be divided by 3, it means the result has 1 on this bit
        # for python if result greater than 2^31, it is negative, change it to negative.
        res = 0
        for i in range(32):
            cnt = 0
            bit = 1 << i
            for num in nums:
                cnt += num & bit
            if cnt % 3 != 0:
                res |= bit
        return self.convert(res)

    def convert(self, x):
        if x >= 2 ** 31:
            x -= 2 ** 32
        return x