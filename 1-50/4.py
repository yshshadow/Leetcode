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
        length = len(nums1) + len(nums2)
        target, extra = divmod(length, 2)
        if extra == 0:
            a = self.search(nums1, nums2, target)
            b = self.search(nums1, nums2, target - 1)
            return (a + b) / 2.0
        else:
            return self.search(nums1, nums2, target)

    def search(self, nums1, nums2, target):
        pass
        # i, j = 0, 0
        # while i + j <= target:

