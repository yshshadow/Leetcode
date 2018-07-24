# Given an unsorted integer array, find the smallest missing positive integer.
#
# Example 1:
#
# Input: [1,2,0]
# Output: 3
# Example 2:
#
# Input: [3,4,-1,1]
# Output: 2
# Example 3:
#
# Input: [7,8,9,11,12]
# Output: 1
# Note:
#
# Your algorithm should run in O(n) time and uses constant extra space.

class Solution(object):
    def firstMissingPositive(self, nums):
        """
        :type nums: List[int]
        :rtype: int
         Basic idea:
        1. for any array whose length is l, the first missing positive must be in range [1,...,l+1],
            so we only have to care about those elements in this range and remove the rest.
        2. we can use the array index as the hash to restore the frequency of each number within
             the range [1,...,l+1]
        """
        # nums.append(0)
        # n = len(nums)
        # for i in range(len(nums)):  # delete those useless elements
        #     if nums[i] < 0 or nums[i] >= n:
        #         nums[i] = 0
        # for i in range(len(nums)):  # use the index as the hash to record the frequency of each number
        #     nums[nums[i] % n] += n
        # for i in range(1, len(nums)):
        #     if nums[i] / n == 0:
        #         return i
        # return n

        idx = 0
        while idx < len(nums):
            if nums[idx] > 0 and nums[idx] != idx + 1 and nums[idx] <= len(nums) and nums[nums[idx]-1]!=nums[idx]:
                temp = nums[nums[idx] - 1]
                nums[nums[idx] - 1] = nums[idx]
                nums[idx] = temp
            else:
                idx += 1
        for idx in range(len(nums)):
            if nums[idx] != idx + 1:
                return idx + 1
        return len(nums) + 1


s = Solution()
print(s.firstMissingPositive([1,2,0]))
