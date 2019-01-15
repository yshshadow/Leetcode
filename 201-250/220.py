# Given an array of integers, find out whether there are two distinct indices i and j in the array such that the absolute difference between nums[i] and nums[j] is at most t and the absolute difference between i and j is at most k.
#
# Example 1:
#
# Input: nums = [1,2,3,1], k = 3, t = 0
# Output: true
# Example 2:
#
# Input: nums = [1,0,1,1], k = 1, t = 2
# Output: true
# Example 3:
#
# Input: nums = [1,5,9,1,5,9], k = 2, t = 3
# Output: false
import bisect


class Solution(object):
    def containsNearbyAlmostDuplicate(self, nums, k, t):
        """
        :type nums: List[int]
        :type k: int
        :type t: int
        :rtype: bool
        """
        # tle
        # if len(nums) < 2 or k == 0:
        #     return False
        # sub = None
        # for i in range(len(nums)):
        #     cur = nums[i]
        #     if not sub:
        #         sub = nums[i - k:i] + nums[i + 1:i + k + 1]
        #         sub.sort()
        #     else:
        #         sub.remove(cur)
        #         if i + k < len(nums):
        #             bisect.insort(sub, nums[i + k])
        #     for num in sub:
        #         if cur - t <= num <= cur + t:
        #             return True
        #     if i - k >= 0:
        #         sub.remove(nums[i - k])
        #     bisect.insort(sub, cur)
        # return False

        # bucket sort
        if len(nums) <= 1 or k == 0 or t < 0:
            return False
        bucket = {}
        t += 1
        for i, num in enumerate(nums):
            key = num // t
            if key in bucket:
                return True
            if key - 1 in bucket and abs(bucket[key - 1] - num) < t:
                return True
            if key + 1 in bucket and abs(bucket[key + 1] - num) < t:
                return True
            bucket[key] = num
            if i >= k:
                del bucket[nums[i - k] // t]
        return False


s = Solution()
print(s.containsNearbyAlmostDuplicate([1, 5, 9, 1, 5, 9],
                                      2,
                                      3))
