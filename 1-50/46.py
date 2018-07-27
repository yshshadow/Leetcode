# Given a collection of distinct integers, return all possible permutations.
#
# Example:
#
# Input: [1,2,3]
# Output:
# [
#   [1,2,3],
#   [1,3,2],
#   [2,1,3],
#   [2,3,1],
#   [3,1,2],
#   [3,2,1]
# ]


class Solution(object):
    def permute(self, nums):
        """
        :type nums: List[int]
        :rtype: List[List[int]]
        """
        res = []
        res += self.permute1(nums, [])
        return res

    def permute1(self, nums, visited):
        if len(visited) == len(nums):
            return [list(visited)]  # copy visited
        res = []
        for num in filter(lambda x: x not in visited, nums):
            visited.append(num)
            res += self.permute1(nums, visited)
            visited.remove(num)
        return res


s = Solution()
print(s.permute([1, 2, 3]))
