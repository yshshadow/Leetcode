# Given two arrays, write a function to compute their intersection.
#
# Example 1:
#
# Input: nums1 = [1,2,2,1], nums2 = [2,2]
# Output: [2]
# Example 2:
#
# Input: nums1 = [4,9,5], nums2 = [9,4,9,8,4]
# Output: [9,4]
# Note:
#
# Each element in the result must be unique.
# The result can be in any order.
import bisect


class Solution(object):
    def intersection(self, nums1, nums2):
        """
        :type nums1: List[int]
        :type nums2: List[int]
        :rtype: List[int]
        """
        if not nums1 or not nums2 or len(nums1) == 0 or len(nums2) == 0:
            return []
        # hashmap
        # set1 = set(nums1)
        # set2 = set(nums2)
        # res = []
        # for num in set1:
        #     if num in set2:
        #         res.append(num)
        # return res

        # sort
        nums1.sort()
        nums2.sort()
        res = []
        i, j = 0, 0
        while i < len(nums1) and j < len(nums2):
            if nums1[i] == nums2[j]:
                if (i == 0 or nums1[i] != nums1[i - 1]) and (j == 0 or nums2[j] != nums2[j - 1]):
                    res.append(nums1[i])
                i += 1
                j += 1
            elif nums1[i] > nums2[j]:
                j += 1
            elif nums1[i] < nums2[j]:
                i += 1
        return res
