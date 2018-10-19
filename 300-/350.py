# Given two arrays, write a function to compute their intersection.
#
# Example 1:
#
# Input: nums1 = [1,2,2,1], nums2 = [2,2]
# Output: [2,2]
# Example 2:
#
# Input: nums1 = [4,9,5], nums2 = [9,4,9,8,4]
# Output: [4,9]
# Note:
#
# Each element in the result should appear as many times as it shows in both arrays.
# The result can be in any order.
# Follow up:
#
# What if the given array is already sorted? How would you optimize your algorithm?
# What if nums1's size is small compared to nums2's size? Which algorithm is better?
# What if elements of nums2 are stored on disk, and the memory is limited such that you cannot load all elements into the memory at once?


class Solution(object):
    def intersect(self, nums1, nums2):
        """
        :type nums1: List[int]
        :type nums2: List[int]
        :rtype: List[int]
        """
        if not nums1 or not nums2 or len(nums1) == 0 or len(nums2) == 0:
            return []
        # use hashmap
        # dict1 = {}
        # # dict2 = {}
        # for num in nums1:
        #     if num not in dict1:
        #         dict1[num] = 1
        #     else:
        #         dict1[num] += 1
        # res = []
        # for num in nums2:
        #     if num in dict1 and dict1[num] > 0:
        #         res.append(num)
        #         dict1[num] -= 1
        # return res

        # use sort, better when two array size is not similar or one array store in the disk
        nums1.sort()
        nums2.sort()
        res = []
        i, j = 0, 0
        while i < len(nums1) and j < len(nums2):
            if nums1[i] == nums2[j]:
                # if (i == 0 or nums1[i] != nums1[i - 1]) and (j == 0 or nums2[j] != nums2[j - 1]):
                #     res.append(nums1[i])
                i += 1
                j += 1
            elif nums1[i] > nums2[j]:
                j += 1
            elif nums1[i] < nums2[j]:
                i += 1
        return res