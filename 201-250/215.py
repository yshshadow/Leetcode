# Find the kth largest element in an unsorted array. Note that it is the kth largest element in the sorted order, not the kth distinct element.
#
# Example 1:
#
# Input: [3,2,1,5,6,4] and k = 2
# Output: 5
# Example 2:
#
# Input: [3,2,3,1,2,4,5,5,6] and k = 4
# Output: 4
# Note:
# You may assume k is always valid, 1 ≤ k ≤ array's length.
#

import heapq
class Solution:
    def findKthLargest(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: int
        """
        # sort
        # nums.sort()
        # return nums[-k]
        # heap sort
        # heap = []
        # for num in nums:
        #     if len(heap) < k:
        #         heapq.heappush(heap,num)
        #     else:
        #         if num > heap[0]:
        #             heapq.heappop(heap)
        #             heapq.heappush(heap,num)
        # return heap[0]
        # use quicksort
        l, r = 0, len(nums) - 1
        while l <= r:
            pos = self.partition(nums, l, r)
            if pos == k - 1:
                return nums[pos]
            elif pos < k - 1:
                l = pos + 1
            else:
                r = pos - 1

    def partition(self, nums, l, r):
        pivot = nums[l]
        l += 1
        while l <= r:
            if nums[l] < pivot and nums[r] > pivot:
                nums[l], nums[r] = nums[r], nums[l]
                l += 1
                r -= 1
            while l <= r and nums[r] <= pivot:
                r -= 1
            while l <= r and nums[l] >= pivot:
                l += 1
        nums[r], nums[0] = pivot, nums[r]
        return r

s=Solution()
s.findKthLargest([2,1],1)