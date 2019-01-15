# Given an array of numbers nums, in which exactly two elements appear only once and all the other elements appear exactly twice. Find the two elements that appear only once.
#
# Example:
#
# Input:  [1,2,1,3,2,5]
# Output: [3,5]
# Note:
#
# The order of the result is not important. So in the above example, [5, 3] is also correct.
# Your algorithm should run in linear runtime complexity. Could you implement it using only constant space complexity?

class Solution:
    def singleNumber(self, nums):
        """
        :type nums: List[int]
        :rtype: List[int]
        """
        # use map
        # maps = collections.defaultdict(lambda:0)
        # for num in nums:
        #     maps[num] += 1
        #     if maps[num] == 2:
        #         del maps[num]
        # return [k for k in maps]

        # bit manipulate
        if not nums:
            return []
        xor = nums[0]
        for num in nums[1:]:
            xor ^= num
        xor &= -xor
        p1, p2 = 0, 0
        for num in nums:
            if xor & num:
                p1 ^= num
            else:
                p2 ^= num
        return [p1, p2]
