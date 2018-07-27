# Given a collection of numbers that might contain duplicates, return all possible unique permutations.
#
# Example:
#
# Input: [1,1,2]
# Output:
# [
#   [1,1,2],
#   [1,2,1],
#   [2,1,1]
# ]


class Solution(object):
    def permuteUnique(self, nums):
        """
        :type nums: List[int]
        :rtype: List[List[int]]
        """
        # res = []
        #
        # def permute1(index, visited):
        #     if len(visited) == len(index):
        #         vs = list(visited)
        #         for x, v in enumerate(vs):
        #             vs[x] = nums[v]
        #         return [tuple(vs)]  # copy visited
        #     res = []
        #     for num in filter(lambda x: x not in visited, index):
        #         visited.append(num)
        #         res += permute1(index, visited)
        #         visited.remove(num)
        #     return res
        #
        # res += permute1(range(len(nums)), [])
        # return list(set(res))
        res = []
        self.permute1(nums, res, 0)
        return res

    def permute1(self, nums, res, start):
        if start == len(nums) - 1:
            res.append(list(nums))
            return

        swap = set()
        for x in range(start, len(nums)):
            if nums[x] not in swap:
                swap.add(nums[x])
            else:
                continue
            nums[start], nums[x] = nums[x], nums[start]
            self.permute1(nums, res, start + 1)
            nums[start], nums[x] = nums[x], nums[start]
        return res


s = Solution()
print(s.permuteUnique([1, 1, 2]))
