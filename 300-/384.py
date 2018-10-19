# Shuffle a set of numbers without duplicates.
#
# Example:
#
# // Init an array with set 1, 2, and 3.
# int[] nums = {1,2,3};
# Solution solution = new Solution(nums);
#
# // Shuffle the array [1,2,3] and return its result. Any permutation of [1,2,3] must equally likely to be returned.
# solution.shuffle();
#
# // Resets the array back to its original configuration [1,2,3].
# solution.reset();
#
# // Returns the random shuffling of array [1,2,3].
# solution.shuffle();
import random


class Solution:
    def __init__(self, nums):
        """
        :type nums: List[int]
        """
        self.origin = list(nums)
        self.array = nums

    def reset(self):
        """
        Resets the array to its original configuration and return it.
        :rtype: List[int]
        """
        self.array = self.origin
        self.origin = list(self.origin)
        return self.array

    def shuffle(self):
        """
        Returns a random shuffling of the array.
        :rtype: List[int]
        """
        for i in range(len(self.array)):
            swap = random.randint(i, len(self.array) - 1)
            self.array[swap], self.array[i] = self.array[i], self.array[swap]
        return self.array



            # Your Solution object will be instantiated and called as such:
            # obj = Solution(nums)
            # param_1 = obj.reset()
            # param_2 = obj.shuffle()
