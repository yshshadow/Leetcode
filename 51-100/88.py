# Given two sorted integer arrays nums1 and nums2, merge nums2 into nums1 as one sorted array.
#
# Note:
# You may assume that nums1 has enough space (size that is greater or equal to m + n) to hold additional elements from nums2. The number of elements initialized in nums1 and nums2 are m and n respectively.
#


class Solution:
    def merge(self, nums1, m, nums2, n):
        """
        :type nums1: List[int]
        :type m: int
        :type nums2: List[int]
        :type n: int
        :rtype: void Do not return anything, modify nums1 in-place instead.
        """
        nums1[m: m + n] = nums2  # copy nums2 into nums1
        slow, fast = 0, m
        if m == 0 or n == 0:
            return
        while fast < m + n:
            if nums1[slow] > nums1[fast]:
                temp = nums1[slow]
                nums1[slow] = nums1[fast]
                nums1[fast] = temp
            slow += 1
            if slow == fast:
                fast += 1


s = Solution()
nums1 = [4,5,6,0,0,0]
m = 3
nums2 = [1,2,3]
n = 3
s.merge(nums1, m, nums2, n)
print(nums1)
