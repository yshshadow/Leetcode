# There are two sorted arrays nums1 and nums2 of size m and n respectively.
#
# Find the median of the two sorted arrays. The overall run time complexity should be O(log (m+n)).
#
# Example 1:
# nums1 = [1, 3]
# nums2 = [2]
#
# The median is 2.0
# Example 2:
# nums1 = [1, 2]
# nums2 = [3, 4]
#
# The median is (2 + 3)/2 = 2.5

class Solution:
    def findMedianSortedArrays(self, nums1, nums2):
        """
        :type nums1: List[int]
        :type nums2: List[int]
        :rtype: float
        """
        len = len(nums1) + len(nums2) - 1
        index = (int)(len / 2)
        isOdd = len % 2 == 0
        i, j = 0
        times = 0
        while i < len(nums1) or j < len(nums2):
            if i >= len(nums1):
                j += 1
            elif j >= len(nums2):
                i += 1
            else:
                if nums1[i] <= nums2[j]:
                    i += 1
                else:
                    j += 1
            times += 1
            if times == index:
                break
        if isOdd:
            return
