# The set [1,2,3,...,n] contains a total of n! unique permutations.
#
# By listing and labeling all of the permutations in order, we get the following sequence for n = 3:
#
# "123"
# "132"
# "213"
# "231"
# "312"
# "321"
# Given n and k, return the kth permutation sequence.
#
# Note:
#
# Given n will be between 1 and 9 inclusive.
# Given k will be between 1 and n! inclusive.
# Example 1:
#
# Input: n = 3, k = 3
# Output: "213"
# Example 2:
#
# Input: n = 4, k = 9
# Output: "2314"
import math


class Solution:
    def getPermutation(self, n, k):
        """
        :type n: int
        :type k: int
        :rtype: str
        """
        # dfs solution TLE
        #     res = []
        #     self.helper(list(range(1, n + 1)), [], res)
        #     return res[k - 1]
        #
        # def helper(self, nums, permutation, res):
        #     if len(permutation) == len(nums):
        #         res.append(''.join(permutation))
        #         return
        #     for i in range(0, len(nums)):
        #         char = str(nums[i])
        #         if char in permutation:
        #             continue
        #         self.helper(nums, permutation + [char], res)

        # math solution
        nums = list(range(1, n + 1))
        res = ''
        k -= 1  # permutation start at 1, so k need -1 at first
        while n > 0:
            n -= 1
            idx, k = divmod(k, math.factorial(n))
            res += str(nums[idx])
            nums.remove(nums[idx])
        return res


print(math.factorial(0))
# print(map(str, list(range(1, 3 + 1))))
s = Solution()
print(s.getPermutation(4, 9))
